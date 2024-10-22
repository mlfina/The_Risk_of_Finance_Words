import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn2

## process txt
def read_txt_to_set(file_path):

    data_set = set()
    with open(file_path, 'r') as file:
        for line in file:
            cleaned_line = line.strip()
            if cleaned_line: 
                data_set.add(cleaned_line)    
    return data_set

####################################################
## venn between vol dict and color dict
####################################################

set_vol_pos = read_txt_to_set("data/output/dictionaries/volatility_positive_dictionary_2005_2020.txt")
set_vol_neg = read_txt_to_set("data/output/dictionaries/volatility_negative_dictionary_2005_2020.txt")
set_ret_pos = read_txt_to_set("data/output/dictionaries/color_positive_dictionary.txt")
set_ret_neg = read_txt_to_set("data/output/dictionaries/color_negative_dictionary.txt")
set_LM_pos = read_txt_to_set("data/output/dictionaries/LM_pos.txt")
set_LM_neg = read_txt_to_set("data/output/dictionaries/LM_neg.txt")


####################################################

plt.figure(figsize=(10, 7))
f = venn3([set_vol_pos, set_ret_pos, set_ret_neg], 
                     set_labels=('\n Volatility \n positive \n dictionary', 
                                 '\n Colour \n positive \n dictionary', 
                                 '\n Colour \n negtive \n dictionary'),
                     set_colors=("white", "white", "white"),  
                     alpha=0.8, 
                     normalize_to=1.0
                    )

f.set_labels[0].set_y(-0.40)
f.set_labels[1].set_y(-0.40)
f.set_labels[2].set_y(-0.40)
for text in f.set_labels:
    text.set_fontsize(20)
for text in [f.get_label_by_id('100'), 
             f.get_label_by_id('010'), 
             f.get_label_by_id('001'), 
             f.get_label_by_id('101')]:
    text.set_fontsize(20)

f.get_patch_by_id('100').set_edgecolor('black')
f.get_patch_by_id('010').set_edgecolor('black')
f.get_patch_by_id('101').set_edgecolor('black')
f.get_patch_by_id('001').set_edgecolor('black')
plt.savefig('data/output/venn_diagrams/venn_diagrams_vol_colour_pos.pdf', bbox_inches='tight')
plt.show()


####################################################
plt.figure(figsize=(10, 7))
g = venn3(subsets=[set_vol_neg, set_ret_pos, set_ret_neg], 
                        set_labels=('\n Volatility \n negative \n dictionary', 
                                    '\n Colour \n positive \n dictionary', 
                                    '\n Colour \n negtive \n dictionary'),
                        set_colors=("white", "white", "white"),  
                        alpha=0.8, 
                        normalize_to=1.0
                        )

g.set_labels[0].set_y(-0.40)
g.set_labels[1].set_y(-0.40)
g.set_labels[2].set_y(-0.40)
for text in g.set_labels:
    text.set_fontsize(20)
for text in [g.get_label_by_id('100'), 
             g.get_label_by_id('010'), 
             g.get_label_by_id('110'),
             g.get_label_by_id('101'),
             g.get_label_by_id('001')]:
    text.set_fontsize(20)

g.get_patch_by_id('100').set_edgecolor('black')
g.get_patch_by_id('010').set_edgecolor('black')
g.get_patch_by_id('110').set_edgecolor('black')
g.get_patch_by_id('101').set_edgecolor('black')
g.get_patch_by_id('001').set_edgecolor('black')
plt.savefig('data/output/venn_diagrams/venn_diagrams_vol_colour_neg.pdf', bbox_inches='tight')
plt.show()

####################################################
plt.figure(figsize=(10, 7))
h = venn3(subsets=[set_LM_pos, set_vol_pos, set_LM_neg], 
                        set_labels=('LM \n positive \n dictionary', 
                                    'Volatility \n positive \n dictionary',
                                    'LM \n negtive \n dictionary'),
                        set_colors=("white", "white", "white"),  
                        alpha=0.8, 
                        normalize_to=1.0
                        )

h.set_labels[0].set_x(0.85)
h.set_labels[0].set_y(-0.55)
h.set_labels[1].set_x(0.4)
h.set_labels[1].set_y(-0.55)
h.set_labels[2].set_y(-0.55)
for text in h.set_labels:
    text.set_fontsize(20)
for text in [h.get_label_by_id('100'), 
             h.get_label_by_id('010'), 
             h.get_label_by_id('110'),
             h.get_label_by_id('011'),
             h.get_label_by_id('001')]:
    text.set_fontsize(20)

h.get_patch_by_id('100').set_edgecolor('black')
h.get_patch_by_id('010').set_edgecolor('black')
h.get_patch_by_id('110').set_edgecolor('black')
h.get_label_by_id('110').set_x(0.67)
h.get_label_by_id('110').set_y(0)
h.get_patch_by_id('011').set_edgecolor('black')
h.get_label_by_id('011').set_x(0.3)
h.get_label_by_id('011').set_y(0)
h.get_patch_by_id('001').set_edgecolor('black')

hide_labels = ['110', '011']  
for subset_id in hide_labels:
    h.get_label_by_id(subset_id).set_visible(False)

arrow_props = dict(arrowstyle='->', connectionstyle='arc3,rad=0.5',color='black')
def add_arrow_annotation(ax, label, xy, xytext):
    ax.annotate(label, xy=xy, xytext=xytext,
                arrowprops=arrow_props,
                fontsize=20, ha='center', va='center')

add_arrow_annotation(plt.gca(), h.get_label_by_id('110').get_text(), (0.63, 0), (0.63, -0.3))
add_arrow_annotation(plt.gca(), h.get_label_by_id('011').get_text(), (0.35, 0), (0.35, -0.3))
plt.savefig('data/output/venn_diagrams/venn_diagrams_vol_LM_pos.pdf', bbox_inches='tight')
plt.show()

####################################################

plt.figure(figsize=(10, 7))
k = venn3(subsets=[set_vol_neg, set_LM_pos, set_LM_neg], 
                        set_labels=(
                                    'LM \n positive \n dictionary', 
                                    'Volatility \n negative \n dictionary',
                                    'LM \n negtive \n dictionary'),
                        set_colors=("white", "white", "white"),  
                        alpha=0.8, 
                        normalize_to=1.0
                        )
k.set_labels[0].set_x(-0.84)
k.set_labels[0].set_y(-0.55)
k.set_labels[1].set_x(-0.40)
k.set_labels[1].set_y(-0.55)
k.set_labels[2].set_y(-0.55)
for text in k.set_labels:
    text.set_fontsize(20)
for text in [k.get_label_by_id('100'), 
            k.get_label_by_id('010'), 
            k.get_label_by_id('110'),
            k.get_label_by_id('101'),
            k.get_label_by_id('001')]:
    text.set_fontsize(20)

k.get_patch_by_id('100').set_edgecolor('black')
k.get_patch_by_id('010').set_edgecolor('black')
k.get_patch_by_id('110').set_edgecolor('black')
k.get_label_by_id('110').set_x(-0.65)
k.get_label_by_id('110').set_y(0)
k.get_patch_by_id('101').set_edgecolor('black')
k.get_label_by_id('101').set_x(-0.32)
k.get_label_by_id('101').set_y(0)
k.get_patch_by_id('001').set_edgecolor('black')

hide_labels = ['110', '101']  
for subset_id in hide_labels:
    k.get_label_by_id(subset_id).set_visible(False)

arrow_props = dict(arrowstyle='->', connectionstyle='arc3,rad=0.5',color='black')

def add_arrow_annotation(ax, label, xy, xytext):
    ax.annotate(label, xy=xy, xytext=xytext,
                arrowprops=arrow_props,
                fontsize=20, ha='center', va='center')

add_arrow_annotation(plt.gca(), k.get_label_by_id('110').get_text(), (-0.60, 0), (-0.60, -0.3))
add_arrow_annotation(plt.gca(), k.get_label_by_id('101').get_text(), (-0.35, 0), (-0.35, -0.3))
plt.savefig('data/output/venn_diagrams/venn_diagrams_vol_LM_neg.pdf', bbox_inches='tight')
plt.show()



import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn2

## process txt
def read_txt_to_set(file_path):

    data_set = set()
    with open(file_path, 'r') as file:
        for line in file:
            cleaned_line = line.strip()
            if cleaned_line: 
                data_set.add(cleaned_line)    
    return data_set

# ####################
# ## venn figure A.5
# ####################
# set_vol_pos = read_txt_to_set("data/output/dictionaries/volatility_positive_dictionary_2005_2020.txt")
# set_vol_neg = read_txt_to_set("data/output/dictionaries/volatility_negative_dictionary_2005_2020.txt")
# set_LM_pos = read_txt_to_set("data/output/dictionaries/LM_pos.txt")
# set_LM_neg = read_txt_to_set("data/output/dictionaries/LM_neg.txt")

# set_LM_Uncertainty = read_txt_to_set("data/output/dictionaries/LM_Uncertainty.txt")
# set_LM_Litigious = read_txt_to_set("data/output/dictionaries/LM_Litigious.txt")
# set_LM_Strong_Modal = read_txt_to_set("data/output/dictionaries/LM_Strong_Modal.txt")
# set_LM_Weak_Modal = read_txt_to_set("data/output/dictionaries/LM_Weak_Modal.txt")
# set_LM_Constraining = read_txt_to_set("data/output/dictionaries/LM_Constraining.txt")
# set_LM_Complexity = read_txt_to_set("data/output/dictionaries/LM_Complexity.txt")

# ####################################################
# plt.figure(figsize=(10, 7))
# j = venn2(subsets=[set_vol_neg, set_LM_Uncertainty], 
#           set_labels=('''Volatility 
# negative 
# dictionary''',   
#               '''LM 
# Uncertainty 
# dictionary'''
# ),
#           set_colors=("white", "white"),  
#           alpha=0.8, 
#           normalize_to=1.0
#          )

# j.set_labels[0].set_position((-0.80, -0.55))
# j.set_labels[1].set_position((0.45, -0.55))

# for text in j.set_labels:
#     text.set_fontsize(20)
#     text.set_horizontalalignment('center') 

# j.get_patch_by_id('100').set_edgecolor('black')
# j.get_patch_by_id('010').set_edgecolor('black')

# for text in [j.get_label_by_id('100'), 
#              j.get_label_by_id('010')]:
#     text.set_fontsize(20)

# plt.savefig('data/output/venn_diagrams/venn_diagrams_vol_LM_Uncertainty_neg.pdf', bbox_inches='tight')
# plt.show()

# ###################################################
# plt.figure(figsize=(10, 7))
# l = venn2(subsets=[set_vol_pos, set_LM_Uncertainty], 
#           set_labels=( 
# '''Volatility 
# positive 
# dictionary''',
# '''LM 
# Uncertainty 
# dictionary'''
# ),
#           set_colors=("white", "white"),  
#           alpha=0.8, 
#           normalize_to=1.0
#          )

# l.set_labels[0].set_position((-0.45, -0.55))
# l.set_labels[1].set_position((0.3, -0.55))

# for text in l.set_labels:
#     text.set_fontsize(20)
#     text.set_horizontalalignment('center') 

# l.get_patch_by_id('100').set_edgecolor('black')
# l.get_patch_by_id('010').set_edgecolor('black')
# l.get_patch_by_id('110').set_edgecolor('black')

# for text in [l.get_label_by_id('100'), 
#              l.get_label_by_id('010'),
#              l.get_label_by_id('110')]:
#     text.set_fontsize(20)

# plt.savefig('data/output/venn_diagrams/venn_diagrams_vol_LM_Uncertainty_pos.pdf', bbox_inches='tight')
# plt.show()

# ####################################################
# plt.figure(figsize=(10, 7))
# m = venn2(subsets=[set_vol_pos, set_LM_Litigious], 
#           set_labels=( 
# '''Volatility 
# positive 
# dictionary''',
# '''LM 
# Litigious 
# dictionary'''),
#           set_colors=("white", "white"),  
#           alpha=0.8, 
#           normalize_to=1.0
#          )

# m.set_labels[0].set_position((-0.60, -0.55))
# m.set_labels[1].set_position((0.15, -0.55))

# for text in m.set_labels:
#     text.set_fontsize(20)
#     text.set_horizontalalignment('center') 

# m.get_patch_by_id('100').set_edgecolor('black')
# m.get_patch_by_id('010').set_edgecolor('black')
# m.get_patch_by_id('110').set_edgecolor('black')

# for text in [m.get_label_by_id('100'), 
#              m.get_label_by_id('010'),
#              m.get_label_by_id('110')]:
#     text.set_fontsize(20)

# hide_labels = ['110']  
# for subset_id in hide_labels:
#     m.get_label_by_id(subset_id).set_visible(False)

# arrow_props = dict(arrowstyle='->', connectionstyle='arc3,rad=0.5',color='black')
# def add_arrow_annotation(ax, label, xy, xytext):
#     ax.annotate(label, xy=xy, xytext=xytext,
#                 arrowprops=arrow_props,
#                 fontsize=20, ha='center', va='center')

# add_arrow_annotation(plt.gca(), m.get_label_by_id('110').get_text(), (-0.37, 0), (-0.37, -0.3))

# plt.savefig('data/output/venn_diagrams/venn_diagrams_vol_LM_Litigious_pos.pdf', bbox_inches='tight')
# plt.show()

# ####################################################
# plt.figure(figsize=(10, 7))
# m = venn2(subsets=[set_vol_neg, set_LM_Litigious], 
#           set_labels=( 
# '''Volatility 
# negative 
# dictionary''',
# '''LM 
# Litigious 
# dictionary'''),
#           set_colors=("white", "white"),  
#           alpha=0.8, 
#           normalize_to=1.0
#          )

# m.set_labels[0].set_position((-1, -0.55))
# m.set_labels[1].set_position((0.15, -0.55))

# for text in m.set_labels:
#     text.set_fontsize(20)
#     text.set_horizontalalignment('center') 

# m.get_patch_by_id('100').set_edgecolor('black')
# m.get_patch_by_id('010').set_edgecolor('black')

# for text in [m.get_label_by_id('100'), 
#              m.get_label_by_id('010')]:
#     text.set_fontsize(20)

# plt.savefig('data/output/venn_diagrams/venn_diagrams_vol_LM_Litigious_neg.pdf', bbox_inches='tight')
# plt.show()

# ###################################################
# plt.figure(figsize=(10, 7))
# m = venn2(subsets=[set_vol_neg, set_LM_Strong_Modal], 
#           set_labels=( 
# '''Volatility 
# negative 
# dictionary''',
# '''LM 
# Strong Modal 
# dictionary'''),
#           set_colors=("white", "white"),  
#           alpha=0.8, 
#           normalize_to=1.0
#          )

# m.set_labels[0].set_position((-0.12, -0.55))
# m.set_labels[1].set_position((1, -0.55))

# for text in m.set_labels:
#     text.set_fontsize(20)
#     text.set_horizontalalignment('center') 

# m.get_patch_by_id('100').set_edgecolor('black')
# m.get_patch_by_id('010').set_edgecolor('black')

# for text in [m.get_label_by_id('100'), 
#              m.get_label_by_id('010')]:
#     text.set_fontsize(20)

# plt.savefig('data/output/venn_diagrams/venn_diagrams_vol_LM_Strong_Modal_neg.pdf', bbox_inches='tight')
# plt.show()

# ###################################################
# plt.figure(figsize=(10, 7))
# m = venn2(subsets=[set_vol_pos, set_LM_Strong_Modal], 
#           set_labels=(
# '''Volatility 
# positive 
# dictionary''',
# '''LM 
# Strong Modal 
# dictionary'''),
#           set_colors=("white", "white"),  
#           alpha=0.8, 
#           normalize_to=1.0
#          )

# m.set_labels[0].set_position((-0.12, -0.55))
# m.set_labels[1].set_position((1, -0.55))

# for text in m.set_labels:
#     text.set_fontsize(20)
#     text.set_horizontalalignment('center') 

# m.get_patch_by_id('100').set_edgecolor('black')
# m.get_patch_by_id('010').set_edgecolor('black')

# for text in [m.get_label_by_id('100'), 
#              m.get_label_by_id('010')]:
#     text.set_fontsize(20)

# plt.savefig('data/output/venn_diagrams/venn_diagrams_vol_LM_Strong_Modal_pos.pdf', bbox_inches='tight')
# plt.show()


# ###################################################
# plt.figure(figsize=(10, 7))
# m = venn2(subsets=[set_vol_pos, set_LM_Weak_Modal], 
#           set_labels=(
# '''Volatility 
# positive 
# dictionary''',
# '''LM 
# Weak Modal 
# dictionary'''),
#           set_colors=("white", "white"),  
#           alpha=0.8, 
#           normalize_to=1.0
#          )

# m.set_labels[0].set_position((-0.12, -0.55))
# m.set_labels[1].set_position((0.6, -0.55))

# for text in m.set_labels:
#     text.set_fontsize(20)
#     text.set_horizontalalignment('center') 

# m.get_patch_by_id('100').set_edgecolor('black')
# m.get_patch_by_id('010').set_edgecolor('black')
# m.get_patch_by_id('110').set_edgecolor('black')

# for text in [m.get_label_by_id('100'), 
#              m.get_label_by_id('010'),
#              m.get_label_by_id('110')]:
#     text.set_fontsize(20)

# plt.savefig('data/output/venn_diagrams/venn_diagrams_vol_LM_Weak_Modal_pos.pdf', bbox_inches='tight')
# plt.show()


# ####################################################
# plt.figure(figsize=(10, 7))
# m = venn2(subsets=[set_vol_neg, set_LM_Weak_Modal], 
#           set_labels=(
# '''Volatility 
# negative 
# dictionary''',
# '''LM 
# Weak Modal 
# dictionary'''),
#           set_colors=("white", "white"),  
#           alpha=0.8, 
#           normalize_to=1.0
#          )

# m.set_labels[0].set_position((-0.15, -0.55))
# m.set_labels[1].set_position((0.95, -0.55))

# for text in m.set_labels:
#     text.set_fontsize(20)
#     text.set_horizontalalignment('center') 

# m.get_patch_by_id('100').set_edgecolor('black')
# m.get_patch_by_id('010').set_edgecolor('black')

# for text in [m.get_label_by_id('100'), 
#              m.get_label_by_id('010')]:
#     text.set_fontsize(20)

# plt.savefig('data/output/venn_diagrams/venn_diagrams_vol_LM_Weak_Modal_neg.pdf', bbox_inches='tight')
# plt.show()

# ####################################################
# plt.figure(figsize=(10, 7))
# m = venn2(subsets=[set_vol_neg, set_LM_Constraining], 
#           set_labels=(
# '''Volatility 
# negative 
# dictionary''',
# '''LM 
# Constraining 
# dictionary'''),
#           set_colors=("white", "white"),  
#           alpha=0.8, 
#           normalize_to=1.0
#          )

# m.set_labels[0].set_position((-0.65, -0.55))
# m.set_labels[1].set_position((0.55, -0.55))

# for text in m.set_labels:
#     text.set_fontsize(20)
#     text.set_horizontalalignment('center') 

# m.get_patch_by_id('100').set_edgecolor('black')
# m.get_patch_by_id('010').set_edgecolor('black')

# for text in [m.get_label_by_id('100'), 
#              m.get_label_by_id('010')]:
#     text.set_fontsize(20)

# plt.savefig('data/output/venn_diagrams/venn_diagrams_vol_LM_Constraining_neg.pdf', bbox_inches='tight')
# plt.show()

# ####################################################
# plt.figure(figsize=(10, 7))
# m = venn2(subsets=[set_vol_pos, set_LM_Constraining], 
#           set_labels=(
# '''Volatility 
# positive
# dictionary''',
# '''LM 
# Constraining 
# dictionary'''),
#           set_colors=("white", "white"),  
#           alpha=0.8, 
#           normalize_to=1.0
#          )

# m.set_labels[0].set_position((-0.35, -0.55))
# m.set_labels[1].set_position((0.4, -0.55))

# for text in m.set_labels:
#     text.set_fontsize(20)
#     text.set_horizontalalignment('center') 

# m.get_patch_by_id('100').set_edgecolor('black')
# m.get_patch_by_id('010').set_edgecolor('black')
# m.get_patch_by_id('110').set_edgecolor('black')

# for text in [m.get_label_by_id('100'), 
#              m.get_label_by_id('010'),
#              m.get_label_by_id('110')]:
#     text.set_fontsize(20)

# plt.savefig('data/output/venn_diagrams/venn_diagrams_vol_LM_Constraining_pos.pdf', bbox_inches='tight')
# plt.show()

# # ####################################################
# plt.figure(figsize=(10, 7))
# m = venn2(subsets=[set_vol_pos, set_LM_Complexity], 
#           set_labels=(
# '''Volatility 
# positive
# dictionary''',
# '''LM 
# Complexity 
# dictionary'''),
#           set_colors=("white", "white"),  
#           alpha=0.8, 
#           normalize_to=1.0
#          )

# m.set_labels[0].set_position((-0.25, -0.55))
# m.set_labels[1].set_position((0.9, -0.55))

# for text in m.set_labels:
#     text.set_fontsize(20)
#     text.set_horizontalalignment('center') 

# m.get_patch_by_id('100').set_edgecolor('black')
# m.get_patch_by_id('010').set_edgecolor('black')

# for text in [m.get_label_by_id('100'), 
#              m.get_label_by_id('010')]:
#     text.set_fontsize(20)

# plt.savefig('data/output/venn_diagrams/venn_diagrams_vol_LM_Complexity_pos.pdf', bbox_inches='tight')
# plt.show()

# ####################################################
# plt.figure(figsize=(10, 7))
# m = venn2(subsets=[set_vol_neg, set_LM_Complexity], 
#           set_labels=(
# '''Volatility 
# negative
# dictionary''',
# '''LM 
# Complexity 
# dictionary'''),
#           set_colors=("white", "white"),  
#           alpha=0.8, 
#           normalize_to=1.0
#          )

# m.set_labels[0].set_position((-0.2, -0.55))
# m.set_labels[1].set_position((0.55, -0.55))

# for text in m.set_labels:
#     text.set_fontsize(20)
#     text.set_horizontalalignment('center') 

# m.get_patch_by_id('100').set_edgecolor('black')
# m.get_patch_by_id('010').set_edgecolor('black')
# m.get_patch_by_id('110').set_edgecolor('black')

# for text in [m.get_label_by_id('100'), 
#              m.get_label_by_id('010'),
#              m.get_label_by_id('110')]:
#     text.set_fontsize(20)

# plt.savefig('data/output/venn_diagrams/venn_diagrams_vol_LM_Complexity_neg.pdf', bbox_inches='tight')
# plt.show()