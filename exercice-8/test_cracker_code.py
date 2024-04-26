"""Un texte a été chiffré avec une permutation de lettres
(en majuscules uniquement). Chaque lettre est remplacée par
une autre lettre, toujours la même.

Je vous donne un cryptogramme: vous connaissez une phrase chiffrée
avec ce code et sa version déchiffrée, à vous de déchiffrer l'autre
message.

Pour tester, je vous fournis le condensat (hash) du message à cracker.

Coverage: 100% et code testé

Mettez dans votre commit git le code cracké. Le test doit passer.

Ensuite, vous voulez produire vous-mêmes des messages: écrire la fonction.
"""
message_en_clair = "ON ETUDIE UNE FORME DE CODAGE PAR SUBSTITUTION"
message_chiffre = "JW XEDVLX DWX HJYUX VX CJVKBX MKY SDFSELEDELJW"

message_a_cracker = "ZX SXCYXE MJDY CYKCIXY DW CJVX CK YXSEX VX CJWELWDXY K XSSKGXY"

hash_du_message_dechiffre = 'b9aff3021b039a5923d11cb941d314c5ca0acd02'

import hashlib

def encrypt_text(cleartext: str) -> str:
    raise NotImplementedError()

def decrypt_text(encrypted: str) -> str:
    raise NotImplementedError()

def test_crackage():
    assert decrypt_text(message_chiffre) == message_en_clair
    assert hashlib.sha1(decrypt_text(message_a_cracker).encode('utf-8')).hexdigest() == hash_du_message_dechiffre

def test_encodage():
    assert decrypt_text(encrypt_text('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    assert decrypt_text(encrypt_text('BONJOUR LES AMIS')) == 'BONJOUR LES AMIS'