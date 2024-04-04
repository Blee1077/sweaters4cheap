BASE_URL_PAULJAMES = "https://www.pauljamesknitwear.com/products/"

PRODUCT_URLS = [
        "the-fitted-submariner-roll-neck-merino-wool-jumper?variant=43629804880126",
        "the-fitted-submariner-roll-neck-merino-wool-jumper?variant=37772680954048",
        "the-fitted-submariner-roll-neck-merino-wool-jumper?variant=43629856227582",
        "the-fitted-submariner-roll-neck-merino-wool-jumper?variant=37772680790208",
        "mens-100-cotton-fisherman-rib-knit-roll-neck-jumper?variant=41013866365120",
        "mens-100-cotton-fisherman-rib-knit-roll-neck-jumper?variant=44210972459262",
        "mens-100-ultra-fine-cotton-buttonless-polo-shirt?variant=42768727539966",
        "mens-chunky-merino-wool-crew-neck-jumper?variant=44590932918526",
        "mens-100-british-wool-heavyweight-ribbed-jumper?variant=42775292215550",
]

PROD_URL_DICT = {
    'paul_james':[
        BASE_URL_PAULJAMES + url for url in PRODUCT_URLS
    ],
}