import sys
import requests

def main():
    # Vérifier que l'utilisateur a fourni un argument de ligne de commande
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        # Essayer de convertir l'argument en float
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Interroger l'API de CoinDesk pour obtenir le prix actuel du Bitcoin
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        rate_float = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Error fetching data from CoinDesk API")

    # Calculer le coût total
    total_cost = num_bitcoins * rate_float

    # Afficher le coût total avec mise en forme
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
