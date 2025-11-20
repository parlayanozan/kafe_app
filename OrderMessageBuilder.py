from models import Siparis


class SiparisAciklayici:
    ## Sipariş açıklamalarını oluşturan sınıf.
    def aciklama_olustur(self, siparis: Siparis) -> str:
        parcalari = []

        for item in siparis.kullanilanlar:
            adet = str(item.adet)
            ad = item.hammadde.ad
            parca = adet + " doz " + ad 
            parcalari.append(parca)

        tarif = ", ".join(parcalari)

        mesaj = (
            siparis.kahve_adi + " seçtiniz. Bu içeceğimiz " + tarif + " içermektedir. Afiyet olsun."
        )

        return mesaj    