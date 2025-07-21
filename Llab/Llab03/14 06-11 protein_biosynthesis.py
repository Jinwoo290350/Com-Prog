'''
[protein_biosynthesis]
ชีวสังเคราะห์โปรตีน (Protein Biosynthesis) หมายถึง กระบวนการสร้างโปรตีนที่เกิดขึ้นเซลล์ ประกอบด้วย 2 ขั้นตอนหลัก ดังนี้

    1.กระบวนการถอดรหัสพันธุกรรม (Transcription) หมายถึง การสร้าง RNA โดยใช้ DNA เป็นแม่พิมพ์ โดยวิธีการนี้ ข้อความพันธุกรรมบน DNA จะถูกถ่ายทอดไปยัง RNA
    ลําดับเบสมีทั้งหมด 5 ชนิด ได้แก่ Adenine(A), Cytosine(C), Guanine(G), Thymine(T) และ Uracil(U) โดยสามารถพบ A C G T ได้ใน DNA และ A C G U ได้ใน RNA
        ในกระบวนการนี้ เราจะนํา DNA แม่แบบมาสร้างเป็น RNA โดยจะใช้คู่เบสที่พอดีกับคู่เบสของ DNA แม่แบบตามตารางข้างล่าง ดังนั้น หาก DNA แม่แบบเป็น TACATTAAAGGCCC ก็จะได้ RNA เป็น AUGUAAUUUCCGGG

DNA แม่แบบ        RNA
         A                    U
         C                    G
         G                    C
         T                    A

    2.กระบวนการแปลรหัส (Translation) หมายถึงการแปลรหัสข้อมูลพันธุกรรมซึ่งอยู่ในรูปของ RNA ไปเป็นลําดับกรดอะมิโนในกระบวนการสังเคราะห์โปรตีน
        สําหรับกระบวนการนี้จะเริ่มต้นทํางานที่ลําดับเบส AUG (start codon)ซึ่งจะได้กรดอะมิโน methionine และจะสังเคราะห์กรดอะมิโนรอบละ 3 ลําดับเบส และหยุดการสร้างเมื่อพบลําดับเบส
    UAA UGA หรือ UAG (stop codon) ซึ่งลําดับเบสทั้ง 3 แบบนี้จะไม่ให้กรดอะมิโนออกมา ดังนั้น หาก RNA เป็น GCAUGAGCCAGUACACCUAAAGU ก็จะได้กรดอะมิโนทั้งหมด 5 ตัวคือ
    GC[AUG][AGC][CAG][UAC][ACC]UAAAUG
จากสาย DNA ที่กําหนดให้ จงพัฒนาโปรแกรมเพื่อหาจํานวนกรดอะมิโนที่ได้หลังจากผ่านกระบวนการถอดรหัสพันธุกรรม และ กระบวนการแปลรหัสแล้ว รับประกันว่า DNA ที่นําเข้าจะประกอบด้วย ‘A’, ‘C’, ‘G’ และ ‘T’ เท่านั้น และภายใน DNA จะพบ start codon ก่อน stop codon เสมอ และจะถอดเฉพาะสายรหัสแรกสุดที่เจอเท่านั้น

Sample Output 1
DNA: CGTCGTCCTACAGCATGAGCATCATCAGCCCATTGTCATGC
4 Amino acid(s)
Note: รหัส RNA ที่ได้ GCAGCAGG[AUG][UCG][UAC][UCG]UAGUAGUCGGGUAACAGUACG
Sample Output 2
DNA: CGTACAACGCGGACAAGCGTACCTGCATCTACAAA
8 Amino acid(s)
Note: รหัส RNA ที่ได้ GC[AUG][UUG][CGC][CUG][UUC][GCA][UGG][ACG]UAGAUGUUU
'''

Dic = {
    "A": "U",
    "T": "A",
    "C": "G",
    "G": "C"
}

DNA = input("DNA: ").strip()
RNA = ""
for i in DNA:
    if i in Dic:
        RNA += Dic[i]
    else:
        RNA += i

stop_codons = ["UAA", "UGA", "UAG"]

start_pos = RNA.find("AUG")
if start_pos != -1:
    RNA = RNA[start_pos:]
    num = 0
    
    for i in range(0, len(RNA), 3):
        if i + 3 <= len(RNA):
            codon = RNA[i:i+3]
            if codon in stop_codons:
                break
            num += 1

print(f"{num} Amino acid(s)")