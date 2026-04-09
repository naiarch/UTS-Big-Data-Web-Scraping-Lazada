from playwright.sync_api import sync_playwright
import pandas as pd
import time
import random
from datetime import datetime

URL = "https://www.lazada.co.id/dandan-online/?q=All-Products&langFlag=id&from=wangpu&lang=id&pageTypeId=2"

def jalankan_scraper():
    all_data = []

    halaman = 1  
    maksimal_halaman = 50 
    
    with sync_playwright() as p:
        print("🚀 Memanaskan mesin Playwright...")
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()

        while halaman <= maksimal_halaman:
            print(f"\n--- 📄 MEMBUKA HALAMAN {halaman} ---")
            url_halaman_ini = f"{URL}&page={halaman}"
            
            try:
                page.goto(url_halaman_ini, timeout=120000, wait_until="commit")
                print(f"Sinyal diterima, menunggu loading konten...")
                time.sleep(12) 
            except Exception as e:
                print(f"⚠️ Gagal di halaman {halaman} karena koneksi. Kita simpan yang ada dulu.")
                break
                
            print("Menggulir halaman perlahan...")
            for i in range(8):
                page.mouse.wheel(0, 900) 
                time.sleep(random.uniform(3.0, 5.0)) 

            produk_elements = page.locator('[data-qa-locator="product-item"]').all()
            
            if len(produk_elements) == 0:
                print(f"✅ Halaman {halaman} kosong. Selesai!")
                break
                
            print(f"Menemukan {len(produk_elements)} produk. Mengekstrak data...")
            
            for elemen in produk_elements:
                try:
                    teks_mentah = elemen.inner_text().split('\n')
                    nama, harga, harga_origin, diskon = "", "", "", ""
                    jumlah_review, jumlah_terjual, lokasi = "", "", ""
                    
                    elemen_a = elemen.locator('a').first
                    url_produk = elemen_a.get_attribute('href') if elemen_a else ""
                    if url_produk and url_produk.startswith('//'):
                        url_produk = "https:" + url_produk
                        
                    elemen_img = elemen.locator('img').first
                    url_gambar = elemen_img.get_attribute('src') if elemen_img else ""

                    for teks in teks_mentah:
                        teks = teks.strip()
                        if not teks: continue
                        if teks.startswith('Rp'):
                            if not harga: harga = teks
                            else: harga_origin = teks
                        elif '%' in teks: diskon = teks
                        elif 'Terjual' in teks or 'terjual' in teks:
                            jumlah_terjual = teks.replace('Terjual', '').strip()
                        elif '(' in teks and ')' in teks and not jumlah_review:
                            jumlah_review = teks.replace('(', '').replace(')', '').strip()
                        elif any(loc in teks for loc in ['Jakarta', 'Kota', 'Kab.']):
                            lokasi = teks
                        elif len(teks) > 10 and not nama and 'Rp' not in teks:
                            nama = teks

                    all_data.append({
                        "toko": "Dandan Online",
                        "nama_produk": nama,
                        "harga": harga,
                        "harga_origin": harga_origin,
                        "diskon": diskon,
                        "rating": "rating",
                        "jumlah_review": jumlah_review,
                        "jumlah_terjual": jumlah_terjual,
                        "lokasi": lokasi,
                        "kategori": "Kesehatan & Kecantikan",
                        "brand": "Dandan Online",
                        "url_produk": url_produk,
                        "url_gambar": url_gambar,
                        "tanggal_scraping": datetime.now().strftime("%Y-%m-%d")
                    })
                except:
                    continue 

            print(f"Total terkumpul: {len(all_data)} produk.")
            

            halaman += 1 
            
            waktu_jeda = random.uniform(20.0, 30.0) 
            print(f"Istirahat {waktu_jeda:.1f} detik biar koneksi stabil...")
            time.sleep(waktu_jeda)

        browser.close()
        
    df = pd.DataFrame(all_data)
    df.to_csv("lazada_dandan.csv", index=False)
    print("\n🎉 BERHASIL! Data lanjutan disimpan di dataset_dandan_online_lanjutan.csv")

if __name__ == "__main__":
    jalankan_scraper()