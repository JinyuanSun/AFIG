#!/usr/bin/python

# To get the lineage by name using taxonkit for busco chosing

import argparse

from ete3 import NCBITaxa


def get_parser():
    parser = argparse.ArgumentParser(description='To get the lineage by name using taxonkit and chose busco dataset')
    # parser.parse_args()
    parser.add_argument("-n", "--name")
    return parser


def taxonkitWrapper(taxon_name):
    busco_list = ["acidobacteria",
                  "aconoidasida",
                  "actinobacteria",
                  "actinobacteria",
                  "actinopterygii",
                  "agaricales",
                  "agaricomycetes",
                  "alphaproteobacteria",
                  "alteromonadales",
                  "alveolata",
                  "apicomplexa",
                  "aquificae",
                  "arachnida",
                  "archaea",
                  "arthropoda",
                  "ascomycota",
                  "aves",
                  "bacillales",
                  "bacilli",
                  "bacteria",
                  "bacteroidales",
                  "bacteroidetes",
                  "bacteroidia",
                  "basidiomycota",
                  "betaproteobacteria",
                  "boletales",
                  "brassicales",
                  "burkholderiales",
                  "campylobacterales",
                  "capnodiales",
                  "carnivora",
                  "cellvibrionales",
                  "cetartiodactyla",
                  "chaetothyriales",
                  "chlamydiae",
                  "chlorobi",
                  "chloroflexi",
                  "chlorophyta",
                  "chromatiales",
                  "chroococcales",
                  "clostridia",
                  "clostridiales",
                  "coccidia",
                  "coriobacteriales",
                  "coriobacteriia",
                  "corynebacteriales",
                  "cyanobacteria",
                  "cyprinodontiformes",
                  "cytophagales",
                  "cytophagia",
                  "delta-epsilon-subdivisions",
                  "deltaproteobacteria",
                  "desulfobacterales",
                  "desulfovibrionales",
                  "desulfurococcales",
                  "desulfuromonadales",
                  "diptera",
                  "dothideomycetes",
                  "embryophyta",
                  "endopterygota",
                  "enterobacterales",
                  "entomoplasmatales",
                  "epsilonproteobacteria",
                  "euarchontoglires",
                  "eudicots",
                  "euglenozoa",
                  "eukaryota",
                  "eurotiales",
                  "eurotiomycetes",
                  "euryarchaeota",
                  "eutheria",
                  "fabales",
                  "firmicutes",
                  "flavobacteriales",
                  "flavobacteriia",
                  "fungi",
                  "fusobacteria",
                  "fusobacteriales",
                  "gammaproteobacteria",
                  "glires",
                  "glomerellales",
                  "halobacteria",
                  "halobacteriales",
                  "haloferacales",
                  "helotiales",
                  "hemiptera",
                  "hymenoptera",
                  "hypocreales",
                  "insecta",
                  "lactobacillales",
                  "laurasiatheria",
                  "legionellales",
                  "leotiomycetes",
                  "lepidoptera",
                  "liliopsida",
                  "mammalia",
                  "metazoa",
                  "methanobacteria",
                  "methanococcales",
                  "methanomicrobia",
                  "methanomicrobiales",
                  "micrococcales",
                  "microsporidia",
                  "mollicutes",
                  "mollusca",
                  "mucorales",
                  "mucoromycota",
                  "mycoplasmatales",
                  "natrialbales",
                  "neisseriales",
                  "nematoda",
                  "nitrosomonadales",
                  "nostocales",
                  "oceanospirillales",
                  "onygenales",
                  "oscillatoriales",
                  "passeriformes",
                  "pasteurellales",
                  "planctomycetes",
                  "plasmodium",
                  "pleosporales",
                  "poales",
                  "polyporales",
                  "primates",
                  "propionibacteriales",
                  "proteobacteria",
                  "pseudomonadales",
                  "rhizobiales",
                  "rhodobacterales",
                  "rhodospirillales",
                  "rickettsiales",
                  "saccharomycetes",
                  "sauropsida",
                  "selenomonadales",
                  "solanales",
                  "sordariomycetes",
                  "sphingobacteriia",
                  "sphingomonadales",
                  "spirochaetales",
                  "spirochaetes",
                  "spirochaetia",
                  "stramenopiles",
                  "streptomycetales",
                  "streptosporangiales",
                  "sulfolobales",
                  "synechococcales",
                  "synergistetes",
                  "tenericutes",
                  "tetrapoda",
                  "thaumarchaeota",
                  "thermoanaerobacterales",
                  "thermoplasmata",
                  "thermoproteales",
                  "thermoprotei",
                  "thermotogae",
                  "thiotrichales",
                  "tissierellales",
                  "tissierellia",
                  "tremellomycetes",
                  "verrucomicrobia",
                  "vertebrata",
                  "vibrionales",
                  "viridiplantae",
                  "xanthomonadales"]
    ncbi = NCBITaxa()
    tax_id = ncbi.get_name_translator([taxon_name])[taxon_name][0]
    lineage = ncbi.get_lineage(tax_id)
    lineage_list = [taxname.lower() for taxname in ncbi.get_taxid_translator(lineage).values()]
    for taxonclass in lineage_list[::-1]:
        if taxonclass in busco_list:
            return taxonclass


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    spename = args.name.replace("_", " ")
    taxonname = taxonkitWrapper(spename)
    print(taxonname)
