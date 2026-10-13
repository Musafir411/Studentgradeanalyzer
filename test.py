"""
Tələbə Bal Analiz Sistemi

Plan:
    1. CSV faylından tələbə məlumatlarının oxunması
    2. NumPy ilə əsas statistik hesablamalar
    3. Pandas ilə filtrləmə əməliyyatları
    4. Matplotlib ilə vizuallaşdırma
    5. OOP və xəta idarəetməsi (try-except)

Tələb olunan kitabxanalar:
pip install numpy pandas matplotlib
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class TelebeBalAnalizSistemi:
    """
    Tələbə bal məlumatlarını oxuyan, analiz edən,
    filtrləyən və vizuallaşdıran sinif.
    """

    def __init__(self, fayl_yolu: str):
        self.fayl_yolu = fayl_yolu
        self.df = None

    def melumati_oxu(self):
        """CSV faylını oxuyur və DataFrame daxilinə yükləyir."""
        try:
            self.df = pd.read_csv(self.fayl_yolu, encoding="utf-8")

            if self.df.empty:
                raise ValueError("CSV faylı boşdur.")

            gerekli_sutunlar = {"ad", "yas", "ixtisas", "bal"}
            if not gerekli_sutunlar.issubset(self.df.columns):
                raise ValueError(
                    f"CSV faylında tələb olunan sütunlar çatışmır! "
                    f"Gözlənilən sütunlar: {gerekli_sutunlar}"
                )

            self.df["bal"] = pd.to_numeric(self.df["bal"], errors="raise")
            print("Məlumat uğurla oxundu. İlk 5 sətir:\n")
            print(self.df.head())

        except FileNotFoundError:
            print(f"Xəta: '{self.fayl_yolu}' faylı tapılmadı.")
        except pd.errors.EmptyDataError:
            print("Xəta: CSV faylında heç bir məlumat yoxdur.")
        except ValueError as xeta:
            print(f"Məlumat xətası: {xeta}")
        except Exception as e:
            print(f"Gözlənilməz xəta: {e}")

    def statistikalari_hesabla(self):
        """NumPy vasitəsilə əsas statistik göstəriciləri hesablayır."""
        try:
            if self.df is None:
                raise ValueError("Əvvəlcə məlumat oxunmalıdır.")

            ballar = self.df["bal"].to_numpy()

            print("\n" + "=" * 40)
            print("       ƏSAS STATİSTİK GÖSTƏRİCİLƏR")
            print("=" * 40)
            print(f"Orta bal:             {np.mean(ballar):.2f}")
            print(f"Ən yüksək bal:        {np.max(ballar)}")
            print(f"Ən aşağı bal:         {np.min(ballar)}")
            print(f"Standart kənarlaşma:  {np.std(ballar):.2f}")

        except ValueError as xeta:
            print(f"Xəta: {xeta}")
        except Exception as e:
            print(f"Statistika hesablanarkən xəta: {e}")

    def melumati_filtrele(self):
        """Pandas ilə müxtəlif meyarlara görə filtrləmə aparır."""
        try:
            if self.df is None:
                raise ValueError("Əvvəlcə məlumat oxunmalıdır.")

            print("\n" + "=" * 40)
            print("          FİLTRLƏMƏ NƏTİCƏLƏRİ")
            print("=" * 40)

            # 1. Balı 80-dən yuxarı olan tələbələr
            yuksek_ballilar = self.df[self.df["bal"] > 80]
            print(f"\n1. Balı 80-dən yuxarı olanlar ({len(yuksek_ballilar)} nəfər):")
            print(yuksek_ballilar.head())

            # 2. İxtisası 'Süni İntellekt' olanlar
            si_telebeleri = self.df[self.df["ixtisas"] == "Süni İntellekt"]
            print(f"\n2. Süni İntellekt tələbələri ({len(si_telebeleri)} nəfər):")
            print(si_telebeleri.head())

            # 3. Yaşı 22-dən böyük olan tələbələr
            yasi_boyukler = self.df[self.df["yas"] > 22]
            print(f"\n3. Yaşı 22-dən böyük olanlar ({len(yasi_boyukler)} nəfər):")
            print(yasi_boyukler.head())

        except ValueError as xeta:
            print(f"Xəta: {xeta}")
        except Exception as e:
            print(f"Filtrləmə zamanı xəta: {e}")

    def qrafik_qur(self):
        """Məlumatları qrafiklərlə vizuallaşdırır."""
        try:
            if self.df is None:
                raise ValueError("Əvvəlcə məlumat oxunmalıdır.")

            fig, ax = plt.subplots(1, 2, figsize=(13, 5))

            # 1-ci Qrafik: Balların Paylanma Histoqramı
            ax[0].hist(self.df["bal"], bins=10, color="teal", edgecolor="black", alpha=0.7)
            ax[0].set_title("Balların Paylanma Histoqramı")
            ax[0].set_xlabel("Bal Aralığı")
            ax[0].set_ylabel("Tələbə Sayı")
            ax[0].grid(axis="y", linestyle="--", alpha=0.7)

            # 2-ci Qrafik: İxtisaslar üzrə Orta Bal
            ixtisas_ortalamalari = self.df.groupby("ixtisas")["bal"].mean()
            ax[1].bar(ixtisas_ortalamalari.index, ixtisas_ortalamalari.values, color="coral", edgecolor="black")
            ax[1].set_title("İxtisaslar üzrə Orta Bal")
            ax[1].set_xlabel("İxtisas")
            ax[1].set_ylabel("Orta Bal")
            ax[1].tick_params(axis="x", rotation=25)
            ax[1].grid(axis="y", linestyle="--", alpha=0.7)

            plt.tight_layout()
            plt.show()

        except Exception as e:
            print(f"Qrafik çəkilərkən xəta: {e}")

    def butun_analizi_ise_sal(self):
        """Bütün analiz addımlarını ardıcıl icra edir."""
        self.melumati_oxu()
        if self.df is None:
            print("Analiz dayandırıldı.")
            return

        self.statistikalari_hesabla()
        self.melumati_filtrele()
        self.qrafik_qur()


if __name__ == "__main__":
    fayl_adi = "telebe_ballari.csv"
    analizator = TelebeBalAnalizSistemi(fayl_adi)
    analizator.butun_analizi_ise_sal()
