from secp256k1 import PrivateKey, PublicKey
import bech32
import qrcode
import io

nostr_private_key_new = PrivateKey() 
private = nostr_private_key_new.private_key
public_key = nostr_private_key_new.pubkey.serialize()[1:]

public_key_converted_bits = bech32.convertbits(public_key, 8, 5)
print()
print(bech32.bech32_encode("npub", public_key_converted_bits, bech32.Encoding.BECH32))

private_key_converted_bits = bech32.convertbits(private, 8, 5)
print()
print(bech32.bech32_encode("nsec", private_key_converted_bits, bech32.Encoding.BECH32))

npub_qr_code = qrcode.QRCode()
npub_qr_code.add_data(f'{bech32.bech32_encode("npub", public_key_converted_bits, bech32.Encoding.BECH32)}')

nsec_qr_code = qrcode.QRCode()
nsec_qr_code.add_data(f'{bech32.bech32_encode("nsec", private_key_converted_bits, bech32.Encoding.BECH32)}')

print()
print("Public key qrcode")
npub_ascii = io.StringIO()
npub_qr_code.print_ascii(out=npub_ascii)
npub_ascii.seek(0)
print(npub_ascii.read())

print()
print("Private key qrcode")
nsec_ascii = io.StringIO()
nsec_qr_code.print_ascii(out=nsec_ascii)
nsec_ascii.seek(0)
print(nsec_ascii.read())
