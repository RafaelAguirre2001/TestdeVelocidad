# TEST DE VELOCIDAD CON PYTHON USANDO LA LIBRERIA DE SPEEDTEST

import speedtest

def test_speed():
    st = speedtest.Speedtest()
    download_speed = st.download()
    upload_speed = st.upload()
    ping = st.results.ping
    return(download_speed, upload_speed, ping )

if __name__ == '__main__':
    download_speed, upload_speed, ping = test_speed()
    print(f"Download speed: {download_speed / 1_000_000:.2f} Mbps")
    print(f"Upload speed: {upload_speed / 1_000_000:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")