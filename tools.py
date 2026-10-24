import os
from dotenv import load_dotenv
from tavily import TavilyClient

# Charge les variables cachées dans le fichier .env
load_dotenv()

# Récupère la clé API Tavily
tavily_api_key = os.getenv("TAVILY_API_KEY")

# Initialise l'outil Tavily
tavily_client = TavilyClient(api_key=tavily_api_key)

def search_web(query: str):
    """Recherche des informations sur Internet via Tavily."""
    print(f"Recherche en cours pour : '{query}'...")
    
    # Exécute la recherche
    response = tavily_client.search(query=query)
    
    return response

# Petit test pour voir si ça marche
if __name__ == "__main__":
    resultat = search_web("Quelles sont les dernières actualités sur l'IA au Sénégal ?")
    print(resultat)