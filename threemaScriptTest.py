# coding=UTF-8

import unittest
import threemaScript
import re

class TestThreemaScript(unittest.TestCase):

    def test_helloWorld(self):
        value = threemaScript.helloWorld("Hello World")
        self.assertEqual(value, 'Hello World')

    def test_29_6_19(self):
        text = """Straße: Weiherer Straße Haus-Nr.:
Ortsteil=
Ort: 96170 Trabelsdorf - Lisberg
Objekt:
Sachverhalt: Technische Hilfe #T2726#VU#mit PKW
Einsatznummer= T 4.1 190629 1042
Zusatzinformation1: 1
***ENDE DER DATEI***"""
        sachverhalt = threemaScript.extractSachverhalt(text)
        ort = threemaScript.extractOrt(text)
        self.assertEqual(sachverhalt, "Technische Hilfe #T2726#VU#mit PKW")
        self.assertEqual(ort, "Weiherer Straße 96170 Trabelsdorf - Lisberg")

    def test_7_8_19(self):
        text = """Straße: Amselweg Haus-Nr.: 7
Ortsteil= Amselweg
Ort: 96194 Walsdorf - Walsdorf Oberfr
Objekt:
Sachverhalt: Brand #B1111#im Gebäude#Dachstuhl
Einsatznummer= B 4.1 190807 829
Zusatzinformation1: 1
***ENDE DER DATEI***"""
        sachverhalt = threemaScript.extractSachverhalt(text)
        ort = threemaScript.extractOrt(text)
        self.assertEqual(sachverhalt, "Brand #B1111#im Gebäude#Dachstuhl")
        self.assertEqual(ort, "Amselweg 7 96194 Walsdorf - Walsdorf Oberfr")

    def test_4_5_10(self):
        text = """Straße : Steigerwaldstraße Haus-Nr.: 13
Ortsteil :
Ort : 96170 Trabelsdorf - Lisberg
Objekt : 4.1.2 BA-L FF Feuerwehr Trabelsdorf
Sachverhalt: Technische Hilfe #T1510#RD#First Responder
Einsatznummer= T 4.1 190504 700
Zusatzinformation1.: 1
***ENDE DER DATEI***"""
        sachverhalt = threemaScript.extractSachverhalt(text)
        ort = threemaScript.extractOrt(text)
        self.assertEqual(sachverhalt, "Technische Hilfe #T1510#RD#First Responder")
        self.assertEqual(ort, "Steigerwaldstraße 13 96170 Trabelsdorf - Lisberg")

    def test_1_7_19(self):
        text = """Straße: Seeleite Haus-Nr.: 1
Ortsteil= Seeleite
Ort: 96170 Trabelsdorf - Lisberg
Objekt: 4.1.2 BA-L Hotel Landhotel Altes Kurhaus Trabelsdorf
Sachverhalt: Technische Hilfe #R8210#Wasserrettung#1 Person in Wassernot
Einsatznummer= T 4.1 190701 1047
Zusatzinformation1: 1
***ENDE DER DATEI***"""
        sachverhalt = threemaScript.extractSachverhalt(text)
        ort = threemaScript.extractOrt(text)
        self.assertEqual(sachverhalt, "Technische Hilfe #R8210#Wasserrettung#1 Person in Wassernot")
        self.assertEqual(ort, "Seeleite 1 96170 Trabelsdorf - Lisberg")

    def test_6_5_19(self):
        text = """Straße : Hauptstraße Haus-Nr.:
Ortsteil : Hauptstraße
Ort : 96170 Lisberg - Lisberg
Objekt :
Sachverhalt: Sonstige 2017-4.1 Hilfeleistung - Unterstützung Polizei
Einsatznummer= S 4.1 190506 85
Zusatzinformation1.: 0
***ENDE DER DATEI***"""
        sachverhalt = threemaScript.extractSachverhalt(text)
        ort = threemaScript.extractOrt(text)
        self.assertEqual(sachverhalt, "Sonstige 2017-4.1 Hilfeleistung - Unterstützung Polizei")
        self.assertEqual(ort, "Hauptstraße 96170 Lisberg - Lisberg")

    def test_20_12_19(self):
        text = """Straßez Steigerwaldstraße Haus-NI.:
Ortsteilz
Ort: 95l7O Trabelsdort - Lisberg
Objektz
Sachverhaltz Brand #Bl5l5#VeIkehI#LKW / Bus innerorts
Einsatznummer: B 4.l l9l22O l257
Zusatzinformation1c l
***ENDE DER DATEI***"""
        sachverhalt = threemaScript.extractSachverhalt(text)
        ort = threemaScript.extractOrt(text)
        self.assertEqual(sachverhalt, "")
        self.assertEqual(ort, "")

    def test_createThreemaMessage(self):
        sachverhalt = "Achtung es brennt"
        ort = "Schweinestall 7 10000 Bauernhof"
        message = threemaScript.createThreemaMessage(sachverhalt, ort)
        self.assertEqual(message, """Achtung es brennt
Schweinestall 7 10000 Bauernhof""")

if __name__ == '__main__':
    unittest.main()