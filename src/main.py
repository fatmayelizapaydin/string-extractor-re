import re

def analyze_file():
    # 1. Dosya yolunu al
    file_path = input("Analiz edilecek dosyanın yolunu girin: ")
    
    # 2. Desenler (Ne arıyoruz?)
    patterns = {
        "CRITICAL - API Key": r'(?:sk|AIza|token|key|secret)[-_A-Za-z0-9]{15,}',
        "MEDIUM - IP Address": r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
        "LOW - URL": r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    }

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        print("\n--- ANALİZ RAPORU ---")
        for label, pattern in patterns.items():
            matches = set(re.findall(pattern, content))
            print(f"[{label}]: {len(matches)} adet bulundu.")
            for match in matches:
                print(f"  -> {match}")
    except Exception as e:
        print(f"Dosya okunamadı: {e}")

if __name__ == "__main__":
    analyze_file()
