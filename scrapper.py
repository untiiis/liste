import requests
from bs4 import BeautifulSoup

url = "https://ptiptv.com/topic/39-%F0%9F%9A%80-ptiptv-free-iptv-account-%E2%80%93-for-members-only-daily-update/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Au lieu de chercher après le texte, on cherche TOUS les liens (<a>)
    # ou même le texte brut qui ressemble à une URL
    all_text = soup.get_text()
    
    # On cherche tout ce qui commence par http et finit par m3u_plus
    import re
    liens = re.findall(r'http[s]?://\S+m3u_plus', all_text)
    
    if liens:
        print("Liens trouvés :", liens[0])
    else:
        print("Rien trouvé. Le contenu est peut-être caché aux invités.")
        # Debug : Affichez un petit bout de la page pour voir ce que le script voit
        print(soup.text[:500]) 
else:
    print(f"Erreur HTTP : {response.status_code}")
