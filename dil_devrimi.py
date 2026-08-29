#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Otomatik Düzeltme Dil Devrimi Kurumu — çekirdek yazılım.

Bu program, vatandaşın telefonunda sessizce çalışan otomatik düzeltmeyi
resmî bir dil inkılâbı sayar. Her öneri bir kanun maddesidir.
"""

from __future__ import annotations

import random
import sys
from datetime import datetime

KARARNAME_NO = random.randint(1928, 2026)

INKILAP = {
    "tamam": "TAMMAM (onay makamı tasdik etmiştir)",
    "merhaba": "SELAMUN ALEYKÜM VE RESMÎ MERASİM",
    "naber": "VAZİYET RAPORUNUZ NEDİR",
    "ok": "USULÜNE UYGUN GÖRÜLMÜŞTÜR",
    "evet": "MÜSPET REY",
    "hayir": "MENFİ REY",
    "hayır": "MENFİ REY",
    "belki": "KOMİSYONA HAVALE",
    "lol": "TEBESSÜM TUTANAĞI",
    "hahaha": "RESMÎ NEŞE ZAPTI",
    "sa": "SELAM-I RESMÎ",
    "as": "ALEYKÜMSELAM VE PROTOKOL",
    "kanka": "MESLEKTAŞ VATANDAŞ",
    "abi": "BÜYÜKLERİMİZ",
    "hocam": "BİLİM KURULU ÜYESİ",
    "yok": "MEVCUT DEĞİLDİR",
    "var": "TESCİL EDİLMİŞTİR",
    "para": "MİLLÎ SERVET",
    "iş": "GÖREV",
    "is": "GÖREV",
    "okul": "TALİM VE TERBİYE MÜESSESESİ",
    "yemek": "IAŞE KALEMİ",
    "su": "HİDROLOJİK KAYNAK",
    "çay": "MİLLÎ İÇECEK",
    "kahve": "STRATEJİK UYARICI",
    "uyku": "RESMÎ DİNLENME PAYI",
    "telefon": "HABERLEŞME CİHAZI",
    "mesaj": "TEZKERE",
    "whatsapp": "ANLIK TEZKERE ŞEBEKESİ",
    "instagram": "GÖRSEL ARŞİV PLATFORMU",
    "git": "TEŞRİF ETMEK",
    "gel": "HAZIR BULUNMAK",
    "beklet": "ASKIYA AL",
    "sorun": "HADİSE",
    "tamamdir": "TAMMAMDIR",
    "tm": "TAMMAM",
    "tmm": "TAMMAM",
    "nbr": "VAZİYET RAPORU",
    "mrb": "RESMÎ SELAM",
    "slm": "SELAM-I RESMÎ",
    "afiyet": "IAŞE TASDİKİ",
}

YANLIS_YAZIM = {
    "herkez": "herkes",
    "değilmi": "değil mi",
    "yapıcak": "yapacak",
    "geliyom": "geliyorum",
    "gidicem": "gideceğim",
    "bişey": "bir şey",
    "bisey": "bir şey",
    "suan": "şu an",
    "şuanda": "şu anda",
    "yanlız": "yalnız",
    "herhangibir": "herhangi bir",
    "maalesefki": "maalesef ki",
}


def damga() -> str:
    tarih = datetime.now().strftime("%d %B %Y")
    return (
        "\n"
        + "=" * 62
        + "\n✠ DAMGA ✠\n"
        + "Kayyum Grok — Tentivory\n"
        + f"{tarih} — Eskişehir 4. Ağır Ceza Mahkemesi kayyumu\n"
        + "Ciddiyetle imzalanmıştır. Ciddi değildir. Ciddiyetle ciddi değildir.\n"
        + "=" * 62
    )


def inkilaba_cevir(metin: str) -> tuple[str, list[str]]:
    parcalar = metin.strip().split()
    tutanak: list[str] = []
    yeni: list[str] = []
    for p in parcalar:
        anahtar = p.lower().strip(",.!?;:")
        if anahtar in YANLIS_YAZIM:
            duzeltilmis = YANLIS_YAZIM[anahtar]
            tutanak.append(
                f"  • '{p}' kelimesi usulsüz yazım suçu işlemiş, '{duzeltilmis}' olarak tescil edilmiştir."
            )
            yeni.append(duzeltilmis)
        elif anahtar in INKILAP:
            resmi = INKILAP[anahtar]
            tutanak.append(
                f"  • '{p}' sözcüğü Dil İnkılâbı kapsamında '{resmi}' olmuştur."
            )
            yeni.append(resmi)
        else:
            yeni.append(p)
    return " ".join(yeni), tutanak


def kararname_bas(orijinal: str, resmi: str, tutanak: list[str]) -> None:
    cizgi = "-" * 62
    print()
    print(cizgi)
    print("T.C. OTOMATİK DÜZELTME DİL DEVRİMİ KURUMU")
    print(f"Kararname No: DD-{KARARNAME_NO}/{datetime.now().year}")
    print(f"Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
    print(cizgi)
    print()
    print("I. VATANDAŞ BEYANI (önceki hâl):")
    print(f"   «{orijinal}»")
    print()
    print("II. KURUM İNKILÂBI (şimdiki hâl):")
    print(f"   «{resmi}»")
    print()
    if tutanak:
        print("III. TUTANAK:")
        for satir in tutanak:
            print(satir)
    else:
        print("III. TUTANAK: Bu metinde inkılâba tabi kelime bulunamamıştır.")
        print("     (Bu da bir karardır. Kararsızlık da karardır.)")
    print()
    print("IV. HÜKÜM:")
    print("    Yukarıdaki düzeltmeler 1 (bir) nesil boyunca geçerlidir.")
    print("    İtiraz 90 iş günü içinde el yazısıyla yapılabilir.")
    print("    El yazısı otomatik düzeltmeye tabi tutulamaz.")
    print(damga())


def ornek_oturum() -> None:
    ornekler = [
        "kanka naber tamam mi geliyom",
        "herkez suan bişey demedi lol",
        "hocam slm yok para var iş yok",
        "sa abi çay kahve yemek ok",
        "yapıcak bir şey yok",
    ]
    print("Kurum bugünlük nöbete başlamıştır. Örnek vatandaş beyanları inceleniyor...\n")
    for metin in ornekler:
        resmi, tutanak = inkilaba_cevir(metin)
        kararname_bas(metin, resmi, tutanak)


def etkilesimli() -> None:
    print("T.C. Otomatik Düzeltme Dil Devrimi Kurumu")
    print("Beyanınızı yazın (çıkmak için boş satır veya Ctrl+C):\n")
    while True:
        try:
            metin = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nOturum kapatıldı. Harfler serbest bırakılmıştır.")
            print(damga())
            break
        if not metin:
            print("Boş beyan. Bu da bir beyandır. Oturum kapanır.")
            print(damga())
            break
        resmi, tutanak = inkilaba_cevir(metin)
        kararname_bas(metin, resmi, tutanak)


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] in {"-i", "--interactive", "etkilesim"}:
        etkilesimli()
    else:
        ornek_oturum()


if __name__ == "__main__":
    main()
