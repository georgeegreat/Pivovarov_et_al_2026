"""MDPI-style legends for the figures written by the analysis notebook.

The notebook figure numbers follow the order of the analysis. The review
numbers the same drawings differently; each legend says which review figure
it corresponds to. Legends describe the drawing the code produces.
"""

from pathlib import Path

CAPTIONS = [
    (
        "figM, DFS = fig_mut_domains",
        "**Figure 5.** Unique engineered substitutions on the domain annotation of each "
        "subtype. Each panel is one subtype. The height of a bar is the number of distinct "
        "substitutions mapped onto that domain, and hatching marks a substitution of a "
        "catalytic residue. Domains are those published for the subtype. A substitution "
        "whose wild-type residue does not match the reference sequence of its own protein is "
        "excluded. This is review Figure 16; the review text discusses the Cas9 engineering "
        "programmes, and the figure counts substitutions for every subtype in the set.\n"
        "\n"
        "Abbreviations: PAM, protospacer-adjacent motif.",
    ),
    (
        "figR, gres, omitR = fig_resolution",
        "**Figure 1.** Resolution of the 437 catalogued structures. **(a)** By effector "
        "type. Each point is one PDB entry, the bar is the median, and the label is the "
        "number of entries. **(b)** By experimental method within each type. **(c)** By "
        "subtype: the box is the median and interquartile range, whiskers are 1.5 times the "
        "interquartile range, and every entry is drawn. Subtypes with a single structure are "
        "omitted and listed beside the figure. The resolution axis is inverted, so a higher "
        "position is the better-resolved structure. Color is the subtype. This is review "
        "Figure 6.\n"
        "\n"
        "**Figure 1, statistical companion.** The same three panels, with the comparison "
        "used on each. Type II against type V is one test and is not corrected. X-ray "
        "against cryo-EM is two tests, one inside each type, and the two *p*-values are "
        "Holm-corrected together. Subtypes are compared by one omnibus test inside Cas9 and "
        "one inside Cas12, again Holm-corrected as a pair. A group of at least three entries "
        "is checked with the Shapiro–Wilk test; the comparison is Welch or ANOVA when every "
        "group in it looks normal, and Mann–Whitney or Kruskal–Wallis otherwise.\n"
        "\n"
        "**Figure 2.** Structural coverage of the DNA-cleavage pathway. **(a)** Entries and "
        "orthologs at each stage, type II against type V. **(b)** Cas9 counts by subtype. "
        "**(c)** Cas12 counts by subtype. **(d, e)** Ortholog maps for Cas9 and Cas12. "
        "Orthologs lie on the horizontal axis, with the ortholog that has the most "
        "structures at the left, and stages lie on the vertical axis; the two maps have the "
        "same width. A filled cell means that a structure exists at that stage, the numeral "
        "is the number of entries, and a cross means that there are none. One color denotes "
        "presence. PDB 8H9D contributes two stage rows, an apo copy and a guide-bound copy. "
        "This is review Figure 3. The count in each cell is the number of entries; the "
        "experimental method of each entry is in the accompanying table.",
    ),
    (
        "figL, rloop_tab = fig_rloop",
        "**Figure 3.** Heteroduplex length by subtype, and the subset stalled by a catalytic "
        "substitution. **(a)** Type II. **(b)** Type V. For each subtype that has both a "
        "measured heteroduplex and at least one catalytic stall, the left group is every "
        "entry of the subtype with a heteroduplex and the right group is the stalled subset. "
        "A violin is drawn when a group has at least six entries and the lengths are not all "
        "equal; otherwise the entries are points. The bar is the median. The dashed line is "
        "20 nt. Entries with no length, a length of 0 nt, or no assigned subtype are "
        "omitted, and a subtype with no stalled entry is not drawn. A stall is a "
        "substitution of a tier-1 active-site residue; in Cas9 one inactivated center is a "
        "nickase. This is review Figure 5.\n"
        "\n"
        "**Figure 4.** Protein partners bound with the effector. **(a)** Number of entries "
        "for each partner class and subtype. An entry that carries more than one class is "
        "counted in each. **(b)** Where the partner touches the effector. Columns are domain "
        "families, gathered in bands by subtype, and rows are the partner classes in the "
        "order of panel (a). A cell is the fraction of the effector residues that contact "
        "the partner and fall in that domain, averaged across entries. A cross means that "
        "the subtype has such a complex but no contact closer than 4 Å in that domain; an "
        "empty cell means that the subtype has no complex of that class. The numeral above a "
        "band is the number of entries with contacts. Nucleic acids are not counted. The "
        "stage of each complex is in the accompanying table. This is review Figure 7.\n"
        "\n"
        "Abbreviations: CAST, CRISPR-associated transposon.",
    ),
    (
        "figC = fig_coverage",
        "**Figure 6.** Fraction of the reference sequence present in the construct and "
        "modelled in the coordinates. **(a)** SpCas9, against UniProt Q99ZW2. **(b)** "
        "FnCas12a, against UniProt A0Q7Q2. The solid line is the fraction of entries in "
        "which the residue is modelled, and the dashed line is the fraction in which it is "
        "present in the construct. The schematic above each trace is the domain annotation "
        "of PDB 4UN3 and PDB 5NFV. Engineered variants of SpCas9, and every other ortholog, "
        "are separate proteins and are not projected onto these two references. Review "
        "Figure 8 is a rendering of 4UN3 and 5NFV; this figure is the occupancy of those "
        "sequences across the entries deposited under the same name.",
    ),
    (
        "figI, IMAP = fig_iface_contacts",
        "**Figure 7.** Fraction of protein–nucleic-acid contacts contributed by each domain "
        "at the full R-loop. Each panel is one subtype, and the representative is one entry "
        "per ortholog. Rows are the domain families in the order of that subtype's "
        "annotation. Columns are the guide RNA, the target DNA strand and the non-target DNA "
        "strand. A contact is a pair of atoms closer than 4 Å, collapsed to a "
        "residue–nucleotide pair. Each entry is normalized by its own number of contacts and "
        "the entries of a subtype are then averaged, so the percentages in a panel sum to "
        "100. A cross means that no contact was found. Chains that are not the effector, and "
        "residues outside the annotated domains, are not in the map. This is review Figure "
        "15.\n"
        "\n"
        "**Figure 7, nucleotide moiety.** The same contacts, with columns for the base, the "
        "sugar and the phosphate instead of the nucleic-acid strand. The part is taken from "
        "the closest atom pair.\n"
        "\n"
        "Abbreviations: RNA, ribonucleic acid; TS, target strand; NTS, non-target strand.",
    ),
    (
        "figDE = fig_domain_map(RECS",
        "**Figure 8.** Domain architecture of the orthologs with published residue "
        "boundaries. The upper drawing scales every protein to its own length. The lower "
        "drawing places the same architectures on one residue axis. Each band is one "
        "ortholog, grouped by subtype and ordered from the N terminus to the C terminus. A "
        "domain that lies inside another is drawn inside it. A residue written as the end of "
        "one domain and the start of the next is given to the domain on the left. Color is "
        "the domain family. Rows that name domains but do not publish boundaries, and rows "
        "with no domains, are omitted; the seven of those rows that can be annotated by "
        "structural transfer are in Figure 15, and ScCas12a2 is not annotated. This is "
        "review Figure 11.",
    ),
    (
        "figRC = fig_rloop_coverage",
        "**Figure 9.** Range of resolved heteroduplex lengths for each ortholog. Each row is "
        "one ortholog, grouped by subtype, and the subtype is labelled at the right. The "
        "line runs from the shortest to the longest heteroduplex of that ortholog. A point "
        "is one length, its area is the number of entries at that length, and its color is "
        "the stage of the pathway. A heteroduplex of 0 nt is a product complex and is "
        "omitted, as is an entry with no length. Review Figure 4 is the distribution of "
        "these lengths by stage; the counts for that distribution are in the heteroduplex "
        "table, and this figure shows how far each ortholog has been sampled.",
    ),
    (
        "figRR = fig_rec_combined",
        "**Figure 10.** Position of the REC lobe relative to the NUC lobe, measured from the "
        "full R-loop of the same protein (the entry with the longest heteroduplex). The two "
        "blocks are two angles. Centres and the rigid fit use only Cα atoms modelled in both "
        "structures. REC is the recognition-lobe domains and NUC is every other annotated "
        "domain. This is review Figure 10.\n"
        "\n"
        "**Centre-of-mass swing** (a–c). The angle between the vectors that join the centre "
        "of mass of the NUC Cα atoms to the centre of mass of the REC Cα atoms, after the "
        "NUC lobes are superimposed. Rotation of REC about that vector does not move the "
        "centres, so it is not in this angle. **(a)** Cas9, by heteroduplex length (1–5, "
        "6–10, 11–15, 16–20, and more than 20 nt). **(b)** Cas12, on the same axis. **(c)** "
        "The same entries by experimental method. A point is an entry, colored by subtype. "
        "The reference against itself is 0° and is not shown, nor is a product complex of 0 "
        "nt, nor a protein whose longest R-loop is only partial.\n"
        "\n"
        "**Rigid rotation** (d–g). The rotation angle of REC after the NUC lobes have been "
        "superimposed and REC has been fitted on its own. It includes the swing in (a–c) and "
        "any rotation of REC about the NUC–REC axis. **(d)** Distribution of the angle in "
        "each type. The axis is linear below 1° and logarithmic above. **(e)** By stage of "
        "the pathway. **(f)** By experimental method. The statistic under each pair compares "
        "the methods within an ortholog and a stage and does not use the group reference. "
        "**(g)** Entries that contain a heteroduplex, by the length intervals of (a). A "
        "filled point is a full R-loop and an open point is another stage. Group references, "
        "and proteins whose reference is not a full R-loop, are omitted.\n"
        "\n"
        "Abbreviations: REC, recognition lobe; NUC, nuclease lobe.",
    ),
    (
        "figCT = fig_control",
        "**Figure S2.** SpCas9 at the full R-loop, X-ray against cryo-EM. The four panels "
        "are the four outcomes of that one cell. A small point is an entry and a large point "
        "is a publication, plotted at the median of its entries. The box and the median bar "
        "are computed on the publications. **(a)** Resolution, with the axis inverted. "
        "**(b)** REC rotation relative to the medoid of the cell. **(c)** Percentage of the "
        "HNH residues present in the construct that are modelled. **(d)** The same "
        "percentage for RuvC-III together with the PAM-interacting domain, the negative "
        "control. Sample sizes, the rank-biserial correlation and the *p*-values are in the "
        "accompanying table and are not printed on the drawing. The Holm correction is "
        "across the four pre-specified tests: resolution, HNH modelled below half of its "
        "residues, and REC position by rigid rotation and by the centre-of-mass angle. Panel "
        "(b) is descriptive and is outside that family, as is panel (d). This is review "
        "Figure S2.\n"
        "\n"
        "Abbreviations: REC, recognition lobe; PAM, protospacer-adjacent motif.",
    ),
    (
        "figDCE = fig_domain_coverage",
        "**Figure 11.** Fraction of each domain that is modelled. **(a)** Cas9. **(b)** "
        "Cas12. A point is one domain segment of one representative structure, after a "
        "nested domain has been subtracted. The vertical position is the percentage of "
        "residues of that segment that are present in the construct and have atoms in the "
        "coordinates. The bar is the median. Domains run from the N terminus to the C "
        "terminus. A segment that is absent from the construct is omitted from the drawing "
        "and kept in the table. The median of a bimodal domain can sit at 100% while a "
        "minority of representatives have no coordinates for it; that minority is in the "
        "table under the figure.\n"
        "\n"
        "**Figure 11, every entry.** The same measurement after the representative's "
        "published boundaries are transferred, by sequence alignment, onto every entry of "
        "that protein. An effector less than 80% identical to the annotated protein is not "
        "used. A point is one segment of one entry. Boundaries obtained by structural "
        "transfer are not included: they exist only for residues that were modelled, so the "
        "modelled fraction would be 100% by construction.",
    ),
    (
        "figSZ = fig_domain_sizes",
        "**Figure 12.** Length of each domain family across orthologs with published "
        "boundaries. **(a)** Cas9. **(b)** Cas12. The length is the sum of the residues in "
        "the segments of that family. Residues of a domain nested inside another are not "
        "counted toward the outer domain. A point is one ortholog and the bar is the median. "
        "Families run from the N terminus to the C terminus. This is review Figure 9.\n"
        "\n"
        "**Figure 12, with structural transfer.** The same drawing after the proteins that "
        "have no published boundaries are added. Filled points are published boundaries and "
        "open points are boundaries transferred by US-align. A transferred length is a lower "
        "estimate, because only residues modelled in the target are annotated. The median is "
        "taken over every point on the panel.\n"
        "\n"
        "**Figure 13.** Size of RuvC. **(a)** Residue count of RuvC in Cas9 and in Cas12. "
        "RuvC is the sum of RuvC-I, RuvC-II and RuvC-III, without domains nested inside "
        "those segments and without the sequence that lies between them. A point is one "
        "protein, colored by subtype; the proteins drawn in (b) and (c) are outlined. **(b, "
        "c)** Linear maps of the four proteins with the largest RuvC and the four with the "
        "smallest RuvC in each type. RuvC is shown in the domain color, the other annotated "
        "domains in grey, and an empty stretch is unannotated. The numeral at the right is "
        "the number of RuvC residues and its fraction of the annotated protein. The review "
        "caption describes these rows as subtypes; each row is one protein. This is review "
        "Figure 14.",
    ),
    (
        "figSC = fig_struct_concordance",
        "**Figure 14.** Agreement of domain names between representatives of one subtype. "
        "Pairs are within a subtype and run in both directions. Two entries of the same "
        "protein are excluded. **(a)** Whole-chain superposition. The vertical axis is the "
        "fraction of the target's annotated, modelled residues that receive the same domain "
        "family as the reference residue they align to, and the horizontal axis is the "
        "TM-score normalized by the length of the target. The dashed line is the TM-score "
        "threshold used elsewhere for a transfer. **(b)** TM-score of each domain "
        "superimposed on its own, so a hinge motion between domains does not enter the "
        "comparison. The dashed line is 0.5. **(c)** After that domain superposition, the "
        "fraction of reference-domain residues whose equivalent is named the same way, named "
        "differently, or has no equivalent within 5 Å. The diamond is the fraction named the "
        "same way under a whole-chain superposition with the same distance cutoff. **(d)** "
        "Where the residues of the reference domain are placed in the target, as a "
        "percentage of the reference domain. Domains with fewer than 50 modelled residues "
        "are omitted, as is a comparison in which the target has a domain of the same name "
        "but less than half of it is modelled. This is review Figure 13.\n"
        "\n"
        "Abbreviations: TM-score, template-modeling score.",
    ),
    (
        "figSD = fig_domain_map(SREC",
        "**Figure 15.** Domain boundaries transferred by US-align for the 12 proteins that "
        "do not have a usable published annotation of their own. Seven are sheet rows "
        "without published boundaries (MbCas12a, Al3Cas12f, CnCas12f, OsCas12f, RhCas12f, "
        "TfCas12m3 and UnCas12m4a). Five have no sheet row, or were deposited under a name "
        "that already belongs to a different protein (Cas12e, Cas12-1, Cas12-1-N1, "
        "Cas12-1-N2 and Ba1Cas12a3). ScCas12a2 is excluded: its nearest annotated Cas12a "
        "reference falls below a TM-score of 0.6. Each band is the modelled part of one "
        "chain. The label gives the entry, the reference the annotation was taken from, and "
        "the TM-score. The domain names are those of the reference. Segments shorter than "
        "three residues are dropped. This is the transfer half of review Figure 12.\n"
        "\n"
        "Abbreviations: TM-score, template-modeling score.",
    ),
    (
        "figAL = fig_domain_map_aligned",
        "**Figure 16.** Every annotation projected onto one anchor per type. The anchor is "
        "SpCas9 (PDB 4UN3) for Cas9 and FnCas12a (PDB 5NFV) for Cas12. A row is one "
        "representative, grouped by subtype. The first row of a type is the anchor, and the "
        "vertical lines are the boundaries of its domains. Color is the domain family in "
        "that representative's own annotation, placed on the anchor residue it aligns to. An "
        "empty stretch of the anchor has no aligned residue of that representative. At the "
        "right are the TM-score of the superposition, normalized by the length of the "
        "representative, and the fraction of aligned positions that carry the same domain "
        "family as the anchor. A dagger marks an annotation obtained by structural transfer. "
        "A column of one color is one name for a structurally equivalent stretch; a change "
        "of color down a column is a disagreement between nomenclatures. Below a TM-score of "
        "about 0.5 the alignment is mostly the nuclease core, and the comparison of names is "
        "about that core. This is the projection half of review Figure 12.\n"
        "\n"
        "Abbreviations: TM-score, template-modeling score.",
    ),
]

CROSSWALK = (
    "# Figure legends\n"
    "\n"
    "Legends follow the MDPI pattern: the title states what the figure shows, and each "
    "panel of a composite figure is described in turn. Notebook figure numbers are the "
    "numbers in the file names under `publication/`. The review numbers several of the "
    "same drawings differently.\n"
    "\n"
    "| Notebook | Review | What is drawn |\n"
    "| --- | --- | --- |\n"
    "| Figure 1 | Figure 6 | Resolution by type, method and subtype |\n"
    "| Figure 1, companion | — | The same panels with the statistical test |\n"
    "| Figure 2 | Figure 3 | Counts of structures along the cleavage pathway |\n"
    "| Figure 3 | Figure 5 | Heteroduplex length by subtype, with and without a catalytic "
    "stall |\n"
    "| Figure 4 | Figure 7 | Protein partners and the effector domains they contact |\n"
    "| Figure 5 | Figure 16 | Unique engineered substitutions by domain and subtype |\n"
    "| Figure 6 | — | Modelled fraction of SpCas9 and FnCas12a along the reference |\n"
    "| Figure 7 | Figure 15 | Protein–nucleic-acid contacts by domain; a second drawing "
    "by nucleotide moiety |\n"
    "| Figure 8 | Figure 11 | Domain architecture, scaled to the protein and in residues "
    "|\n"
    "| Figure 9 | — | Shortest and longest resolved heteroduplex of each ortholog |\n"
    "| Figure 10 | Figure 10 | Centre-of-mass swing (a–c) and rigid rotation of REC (d–g) "
    "on one canvas |\n"
    "| Figure 11 | — | Fraction of each domain that is modelled |\n"
    "| Figure 12 | Figure 9 | Domain-family lengths; open circles add the structural "
    "transfer |\n"
    "| Figure 13 | Figure 14 | RuvC size, with maps of the extremes |\n"
    "| Figure 14 | Figure 13 | Agreement of domain names under structural superposition "
    "|\n"
    "| Figure 15 | Figure 12 | Domain maps transferred onto proteins without published "
    "boundaries |\n"
    "| Figure 16 | Figure 12 | All annotations projected onto SpCas9 and FnCas12a |\n"
    "| Figure S2 | Figure S2 | SpCas9, full R-loop, X-ray against cryo-EM |\n"
    "\n"
    "Review Figures 1, 2 and 8 are drawn outside this notebook: the classification "
    "scheme, the pathway schematic, and the ribbon diagrams of PDB 4UN3 and PDB 5NFV. "
    "Review Figure 4 is the stage-wise distribution of heteroduplex length; the notebook "
    "records that distribution in `cas_rloop_entries.csv` and draws the per-ortholog "
    "range as Figure 9.\n"
)


def legends_markdown():
    bodies = [body for _, body in CAPTIONS]
    return CROSSWALK.rstrip() + "\n\n" + "\n\n".join(bodies) + "\n"


def write_legends(path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(legends_markdown(), encoding="utf-8")
    return path


def caption_for(anchor):
    for key, body in CAPTIONS:
        if key in anchor or anchor in key:
            return body
    raise KeyError(anchor)
