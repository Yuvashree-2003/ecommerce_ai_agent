import matplotlib.pyplot as plt
import pandas as pd
import io
import base64

def generate_bar_chart(data: list, x_key: str, y_key: str) -> str:
    df = pd.DataFrame(data)
    plt.figure(figsize=(10, 5))
    plt.bar(df[x_key], df[y_key])
    plt.xlabel(x_key)
    plt.ylabel(y_key)
    plt.title(f"{y_key} by {x_key}")
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    return img_base64
