# generate_cert.py
from OpenSSL import crypto

def generate_self_signed_cert():
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 2048)
    
    cert = crypto.X509()
    cert.get_subject().C = "IL"
    cert.get_subject().CN = "ShadowNet Server"
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(365*24*60*60) # תקף לשנה
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha256')
    
    with open("server.crt", "wt") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode())
    with open("server.key", "wt") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode())
        
    print("[+] Certificate and Key generated successfully!")

if __name__ == "__main__":
    # pip install pyopenssl
    try:
        generate_self_signed_cert()
    except ImportError:
        print("Please run: pip install pyopenssl")