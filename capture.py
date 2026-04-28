from playwright.sync_api import sync_playwright
import time

urls = [
    "https://app.powerbi.com/view?r=eyJrIjoiNmQ0ZjJmM2UtNjI4Ny00MTAwLWFjMDktNTVmZDc1YWUxZTA0IiwidCI6IjI5ZTZhYTNhLTljZTItNDVmYS1iYjZhLWZlYWUwMDU2NjVhZiIsImMiOjEwfQ%3D%3D&pageName=d5a79356a4b7dddb3b12",
    "https://app.powerbi.com/view?r=eyJrIjoiNmQ0ZjJmM2UtNjI4Ny00MTAwLWFjMDktNTVmZDc1YWUxZTA0IiwidCI6IjI5ZTZhYTNhLTljZTItNDVmYS1iYjZhLWZlYWUwMDU2NjVhZiIsImMiOjEwfQ%3D%3D&pageName=c59f9a2c316249ebc41d",
    "https://app.powerbi.com/view?r=eyJrIjoiNmQ0ZjJmM2UtNjI4Ny00MTAwLWFjMDktNTVmZDc1YWUxZTA0IiwidCI6IjI5ZTZhYTNhLTljZTItNDVmYS1iYjZhLWZlYWUwMDU2NjVhZiIsImMiOjEwfQ%3D%3D&pageName=71056e5434aeae55990d",
    "https://app.powerbi.com/view?r=eyJrIjoiNmQ0ZjJmM2UtNjI4Ny00MTAwLWFjMDktNTVmZDc1YWUxZTA0IiwidCI6IjI5ZTZhYTNhLTljZTItNDVmYS1iYjZhLWZlYWUwMDU2NjVhZiIsImMiOjEwfQ%3D%3D&pageName=6af54b18951d5ce9bb6c",
    "https://app.powerbi.com/view?r=eyJrIjoiNmQ0ZjJmM2UtNjI4Ny00MTAwLWFjMDktNTVmZDc1YWUxZTA0IiwidCI6IjI5ZTZhYTNhLTljZTItNDVmYS1iYjZhLWZlYWUwMDU2NjVhZiIsImMiOjEwfQ%3D%3D&pageName=9b351f8381ea904cc214",
    "https://app.powerbi.com/view?r=eyJrIjoiNmQ0ZjJmM2UtNjI4Ny00MTAwLWFjMDktNTVmZDc1YWUxZTA0IiwidCI6IjI5ZTZhYTNhLTljZTItNDVmYS1iYjZhLWZlYWUwMDU2NjVhZiIsImMiOjEwfQ%3D%3D&pageName=e1744970a0e90b704012"
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    
    for index, url in enumerate(urls):
        print(f"Mengakses slide {index}...")
        page.goto(url, wait_until='load')
        
        # Tambahkan waktu tunggu 15 detik agar Power BI benar-benar selesai render & pindah tab
        page.wait_for_timeout(15000) 
        
        page.screenshot(path=f'slide{index}.png', full_page=True)
        print(f"Berhasil menyimpan slide{index}.png")
        
    browser.close()
