from googletrans import Translator
translator=Translator()

def startTranslate(text,src,dest):
    trans=translator.translate(text,src=src,dest=dest)
    print(trans)
    return trans

#this function detects lang automatically and translates to en
def autoTranslateEn(text):
    trans=translator.translate(text)
    print(trans)
    return trans

#this fuction detects lang automatically and translated to dest lang
def autoTranslate(text,dest):
    trans=translator.translate(text,dest=dest)
    print(trans)
    return trans


if __name__ == "__main__":
    autoTranslate("This is a demo of translate",dest="es")

#language codes
# Abkhazian	ab	abk
# Afar	aa	aar
# Afrikaans	af	afr
# Albanian	sq	alb/sqi*
# Amharic	am	amh
# Arabic	ar	ara
# Aragonese	an	arg
# Armenian	hy	arm/hye*
# Assamese	as	asm
# Avestan	ae	ave
# Aymara	ay	aym
# Azerbaijani	az	aze
# Bashkir	ba	bak
# Basque	eu	baq/eus*
# Belarusian	be	bel
# Bengali	bn	ben
# Bihari	bh	bih
# Bislama	bi	bis
# Bosnian	bs	bos
# Breton	br	bre
# Bulgarian	bg	bul
# Burmese	my	bur/mya*
# Catalan	ca	cat
# Chamorro	ch	cha
# Chechen	ce	che
# Chinese	zh	chi/zho*
# Church Slavic; Slavonic; Old Bulgarian	cu	chu
# Chuvash	cv	chv
# Cornish	kw	cor
# Corsican	co	cos
# Croatian	hr	scr/hrv*
# Czech	cs	cze/ces*
# Danish	da	dan
# Divehi; Dhivehi; Maldivian	dv	div
# Dutch	nl	dut/nld*
# Dzongkha	dz	dzo
# English	en	eng
# Esperanto	eo	epo
# Estonian	et	est
# Faroese	fo	fao
# Fijian	fj	fij
# Finnish	fi	fin
# French	fr	fre/fra*
# Gaelic; Scottish Gaelic	gd	gla
# Galician	gl	glg
# Georgian	ka	geo/kat*
# German	de	ger/deu*
# Greek, Modern (1453-)	el	gre/ell*
# Guarani	gn	grn
# Gujarati	gu	guj
# Haitian; Haitian Creole	ht	hat
# Hausa	ha	hau
# Hebrew	he	heb
# Herero	hz	her
# Hindi	hi	hin
# Hiri Motu	ho	hmo
# Hungarian	hu	hun
# Icelandic	is	ice/isl*
# Ido	io	ido
# Indonesian	id	ind
# Interlingua (International Auxiliary Language Association)	ia	ina
# Interlingue	ie	ile
# Inuktitut	iu	iku
# Inupiaq	ik	ipk
# Irish	ga	gle
# Italian	it	ita
# Japanese	ja	jpn
# Javanese	jv	jav
# Kalaallisut	kl	kal
# Kannada	kn	kan
# Kashmiri	ks	kas
# Kazakh	kk	kaz
# Khmer	km	khm
# Kikuyu; Gikuyu	ki	kik
# Kinyarwanda	rw	kin
# Kirghiz	ky	kir
# Komi	kv	kom
# Korean	ko	kor
# Kuanyama; Kwanyama	kj	kua
# Kurdish	ku	kur
# Lao	lo	lao
# Latin	la	lat
# Latvian	lv	lav
# Limburgan; Limburger; Limburgish	li	lim
# Lingala	ln	lin
# Lithuanian	lt	lit
# Luxembourgish; Letzeburgesch	lb	ltz
# Macedonian	mk	mac/mkd*
# Malagasy	mg	mlg
# Malay	ms	may/msa*
# Malayalam	ml	mal
# Maltese	mt	mlt
# Manx	gv	glv
# Maori	mi	mao/mri*
# Marathi	mr	mar
# Marshallese	mh	mah
# Moldavian	mo	mol
# Mongolian	mn	mon
# Nauru	na	nau
# Navaho, Navajo	nv	nav
# Ndebele, North	nd	nde
# Ndebele, South	nr	nbl
# Ndonga	ng	ndo
# Nepali	ne	nep
# Northern Sami	se	sme
# Norwegian	no	nor
# Norwegian Bokmal	nb	nob
# Norwegian Nynorsk	nn	nno
# Nyanja; Chichewa; Chewa	ny	nya
# Occitan (post 1500); Provencal	oc	oci
# Oriya	or	ori
# Oromo	om	orm
# Ossetian; Ossetic	os	oss
# Pali	pi	pli
# Panjabi	pa	pan
# Persian	fa	per/fas*
# Polish	pl	pol
# Portuguese	pt	por
# Pushto	ps	pus
# Quechua	qu	que
# Raeto-Romance	rm	roh
# Romanian	ro	rum/ron*
# Rundi	rn	run
# Russian	ru	rus
# Samoan	sm	smo
# Sango	sg	sag
# Sanskrit	sa	san
# Sardinian	sc	srd
# Serbian	sr	scc/srp*
# Shona	sn	sna
# Sichuan Yi	ii	iii
# Sindhi	sd	snd
# Sinhala; Sinhalese	si	sin
# Slovak	sk	slo/slk*
# Slovenian	sl	slv
# Somali	so	som
# Sotho, Southern	st	sot
# Spanish; Castilian	es	spa
# Sundanese	su	sun
# Swahili	sw	swa
# Swati	ss	ssw
# Swedish	sv	swe
# Tagalog	tl	tgl
# Tahitian	ty	tah
# Tajik	tg	tgk
# Tamil	ta	tam
# Tatar	tt	tat
# Telugu	te	tel
# Thai	th	tha
# Tibetan	bo	tib/bod*
# Tigrinya	ti	tir
# Tonga (Tonga Islands)	to	ton
# Tsonga	ts	tso
# Tswana	tn	tsn
# Turkish	tr	tur
# Turkmen	tk	tuk
# Twi	tw	twi
# Uighur	ug	uig
# Ukrainian	uk	ukr
# Urdu	ur	urd
# Uzbek	uz	uzb
# Vietnamese	vi	vie
# Volapuk	vo	vol
# Walloon	wa	wln
# Welsh	cy	wel/cym*
# Western Frisian	fy	fry
# Wolof	wo	wol
# Xhosa	xh	xho
# Yiddish	yi	yid
# Yoruba	yo	yor
# Zhuang; Chuang	za	zha
# Zulu	zu	zul