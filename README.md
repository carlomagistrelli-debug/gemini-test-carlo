# System Info CLI 🚀

Una semplice utility Python per monitorare le risorse di sistema in tempo reale direttamente dal terminale, con un'interfaccia tabellare elegante e colorata.

## Caratteristiche
- 📊 **Monitoraggio CPU**: Percentuale di utilizzo istantanea.
- 🧠 **Monitoraggio RAM**: Percentuale di utilizzo e memoria disponibile.
- 💾 **Stato Disco**: Spazio libero e totale sulla partizione root.
- 🎨 **Interfaccia Colorata**: Output formattato in tabelle grazie alla libreria `rich`.

## Requisiti
- Python 3.12+
- `psutil`
- `rich`

## Installazione

1. **Clona il repository**:
   ```bash
   git clone <il-tuo-url-repository>
   cd gemini_test
   ```

2. **Crea un ambiente virtuale** (consigliato):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Installa le dipendenze**:
   ```bash
   pip install psutil rich
   ```

## Utilizzo
Assicurati che l'ambiente virtuale sia attivo, quindi esegui:
```bash
python3 info_sistema.py
```

## Licenza
Questo progetto è distribuito sotto licenza MIT.
