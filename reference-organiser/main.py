import docx
from docx.opc.constants import RELATIONSHIP_TYPE as RT

reverse_mode = True

doc = docx.Document('Test.docx')
rels = doc.part.rels
print(len(rels))
def iter_hyperlink_rels(rels):
    for rel in rels:
        print("REL:", rels[rel].reltype)
        if rels[rel].reltype == RT.HYPERLINK:
            print(rels[rel]._target)

iter_hyperlink_rels(rels)
# for num in range(18, 47):
#     print(doc.paragraphs[num].text)