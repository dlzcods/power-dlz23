# Assuming the package is named 'laundryCode' and the script is named 'hitungHarga.py'
from laundryCode.hitungHarga import hargaBayar

def main():
    print("Selamat datang di Laundry Berkah Jaya!")
    print("==============================\n")

    # Pelanggan 1
    print("Pelanggan 1:")
    customer1 = hargaBayar(1, 3, 5)  # Paket Cuci Kering Lipat, 3 hari, 5 kg
    total_bayar = customer1.hitungTotal()
    print(f"Total Bayar: Rp {total_bayar:.2f}\n")

    # Pelanggan 2
    print("Pelanggan 2:")
    customer2 = hargaBayar(2, 2, 4)  # Paket Cuci Kering Setrika, 2 hari, 4 kg
    total_bayar = customer2.hitungTotal()
    print(f"Total Bayar: Rp {total_bayar:.2f}\n")

    # Pelanggan 3
    print("Pelanggan 3:")
    customer3 = hargaBayar(3, 1, 7)  # Paket Lengkap Kilat, 1 hari, 7 kg
    total_bayar = customer3.hitungTotal()
    print(f"Total Bayar: Rp {total_bayar:.2f}\n")

    # Pelanggan 4
    print("Pelanggan 4:")
    customer4 = hargaBayar(4, 1, 2)  # Paket Express, 1 hari, 2 kg
    total_bayar = customer4.hitungTotal()
    print(f"Total Bayar: Rp {total_bayar:.2f}\n")

    print("Terima kasih telah menggunakan jasa Laundry XYZ!")

if __name__ == "__main__":
    main()