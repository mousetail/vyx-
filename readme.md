# What is this?

This is a attempt to compress vyxal code. It's a huffman tree compressor trained on 1500 Vyxal programs from [CSGE](https://codegolf.stackexchange.com).

# How good is it?

Medium

<!-- INSERT AUTO GENERATED TABLE HERE -->

## Overall

| N=1831 | Original |  Compressed | Difference | Ratio |
| -- | -- | -- | -- | -- |
| mean | [31.12](https://codegolf.stackexchange.com/questions/253125] <!-- ∆/`λƛ h⁼Ǐ¢Ṗλ₇ of λ× ¬ẋ Ȧ⇩ is Π
 -->) | [26.24](https://codegolf.stackexchange.com/questions/252105] <!-- k⁰kv":ɾJJƒ*‛ß+k⁰⇧1Ṁ$‡‛eijøṙ
 -->) | [-4.87](https://codegolf.stackexchange.com/questions/250567] <!-- `⌐÷:aBk⁋+›bḢ¨£ßN∑kTtp+q‛:Ė+,helloworld`:Ė
 -->) | [0.92](https://codegolf.stackexchange.com/questions/229258] <!-- ð₴-0∴`\|/`Ẏ,(\(₴¹n->\)-2↳3¹+n+⁰<-,
 -->) |
| stdev | [191.14](https://codegolf.stackexchange.com/questions/235708] <!-- \o\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"fLkZ:\o\o"\o"fL%"¯∑\o\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"\o"fL%Ė
 -->) | [131.28](https://codegolf.stackexchange.com/questions/235748] <!-- ,₴…‹›⟇+*/-d↵EǍ½ƒɖ1234567890ø∆e₈₇∞₆₄JpiẎȯhtḢṪḣṫ¡Þ₀₁C!¬⇧İN⇩Ż÷«»`;¥£¾¼⅛%→←"ẋ¤ȦFȧ⌐m⊍g≬\ṡ∷‡⁽⟨|⟩‟„$∇_yǏṘRq꘍₍₌Π⁺ʀ↑↓G↲↳⋏⋎Ṅ⁋ð×‛√²⌈⌊:ḊD
 -->) | [92.76](https://codegolf.stackexchange.com/questions/226832] <!-- »⌐ṫżṫṗƛ&%≠ɽ_~ẇ*⁼3L ≈;n~U7⋏₇ḭǔ°₁>Aµ1I(□]:ȯ≤KWƒʁY•₇⟩-RCa⟨&8ẋżṫẏL_ġN⇧ṗḞΠṄẇ%¨ḃ₆Q<Zǒ,]„∨TC⁋⟩`ɾOn^≬İ¾¨Ṫlṅ^£†i-ẏ₂↓∷×ṘǍ¶G?∑x∪ż∪İɖ¹p*₴Ḣ≈J₀↳₁‡x⌈↳D4xJḢmḃẇDpeH&⋏¹!≥₇∑;↑≬m†¥⁋†₇,Ż∪ß^ċ¡}GBİ£:U~ʁ⌈∴Ṡ^ṗ⁺Ȯo↓Ṅ%Ẏṗ§∴ḭ₈Ṁ‛∑ø≈dOƒ¥¤ɖ4Ẏ{⅛I∞_uė∇ṫḭB?U≤ǔ9F⟑q₴ẆŀṠz∞₁XṖ¨‛₇VB₁τḟAsżǒxP∵9)&∵β"Ż∆ ↲,₴øxJT.t꘍/₴ǎpe↔ḟqȯ(^≥Vḭ⁰Ȯɽτ∆ṙ°÷lW≠⇧Cb≠²∩]±ḭy∧D℅øJǔ₅⅛EGḭ≥ẋZ≥×8nΠḋ⟩)Ṗv‹'⇧@jq≥ḟ⁽]¾fǎ⅛Ȯ⌊bDa^ṀP;}ṫ⁼τ1„√ɽh⇩GW€⁼[6¼U~j_IṘ†gJ↔Ȧ$°§_„)Ż"₅‡xußġ₃ǔ↔×ɖɖ[æ¥s‹⁰≈c†t‹ṪṙḊ꘍bεβ¶∩∩{ǒḢġ†₅⟨L⌐∨H»`! `τ75ẇ
 -->) | [0.10](https://codegolf.stackexchange.com/questions/235671] <!-- !¬¬⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧kA!¬⇧wİ÷Ė!¬⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧kA!¬⇧wİ÷Ė
 -->) |
| min | [0.00](https://codegolf.stackexchange.com/questions/231333] <!--  -->) | [0.00](https://codegolf.stackexchange.com/questions/231333] <!--  -->) | [-3680.00](https://codegolf.stackexchange.com/questions/235671] <!-- !¬¬⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧kA!¬⇧wİ÷Ė!¬⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧⇧kA!¬⇧wİ÷Ė
 -->) | [0.00](https://codegolf.stackexchange.com/questions/231333] <!--  -->) |
| 10% med | [4.00](https://codegolf.stackexchange.com/questions/253500] <!-- ²øf
 -->) | [3.00](https://codegolf.stackexchange.com/questions/253389] <!-- 2-1
 -->) | [-3.00](https://codegolf.stackexchange.com/questions/253239] <!-- `æ⁽ æ∴Ǐ₇ ⟑∵ ƛ∪ λ† ¬λ λ⟨ he ¬ṙ ↔Ẏ λ» ∨⁺`»→⇩d»₆τẎ\.+
 -->) | [0.80](https://codegolf.stackexchange.com/questions/253476] <!-- 0ṡṅL
 -->) |
| 25% med | [6.00](https://codegolf.stackexchange.com/questions/253739] <!-- vΠ₆↳›
 -->) | [5.00](https://codegolf.stackexchange.com/questions/253720] <!-- λvxΠ›
 -->) | [-1.00](https://codegolf.stackexchange.com/questions/253794] <!-- ɾ:∑p²ƒ-
 -->) | [0.87](https://codegolf.stackexchange.com/questions/251182] <!-- ʀ:v꘍vvS:fÞGL↳⁋
 -->) |
| median | [10.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [9.00](https://codegolf.stackexchange.com/questions/253810] <!-- ⁽Tẇ∑N₀%J
 -->) | [-1.00](https://codegolf.stackexchange.com/questions/253794] <!-- ɾ:∑p²ƒ-
 -->) | [0.92](https://codegolf.stackexchange.com/questions/253719] <!-- ⌊d-‹Ė)1Ḟ:NY‹
 -->) |
| 75% med | [19.00](https://codegolf.stackexchange.com/questions/253068] <!-- `!±∵ ,∴İ``İ∴, ∵±!`
 -->) | [18.00](https://codegolf.stackexchange.com/questions/253068] <!-- `!±∵ ,∴İ``İ∴, ∵±!`
 -->) | [0.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [1.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) |
| 90% med | [48.00](https://codegolf.stackexchange.com/questions/248228] <!-- \/16꘍¦øṀ÷\|16꘍m:`|  @Hy∧‛NeꜝṘ⋏⇩ ÷… λǐ!  |`WḂḢRJ
 -->) | [44.80](https://codegolf.stackexchange.com/questions/246489] <!-- 1=[\_‛|\"|2≠[⇩ʁ(⁰Ifn\\Ȧ¤j)]‛\_⁰r:t⁰ẋ:£W\|vp¥p]vøṀ
 -->) | [0.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [1.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) |
| max | [6553.00](https://codegolf.stackexchange.com/questions/233768] <!-- aaaabbabaabcbabccabcaabcdbabcdcabcddabcdaabcdebabcdecabcdedabcdeeabcdeaabcdefbabcdefcabcdefdabcdefeabcdeffabcdefaabcdefgbabcdefgcabcdefgdabcdefgeabcdefgfabcdefggabcdefgaabcdefghbabcdefghcabcdefghdabcdefgheabcdefghfabcdefghgabcdefghhabcdefghaabcdefghibabcdefghicabcdefghidabcdefghieabcdefghifabcdefghigabcdefghihabcdefghiiabcdefghiaabcdefghijbabcdefghijcabcdefghijdabcdefghijeabcdefghijfabcdefghijgabcdefghijhabcdefghijiabcdefghijjabcdefghijaabcdefghijkbabcdefghijkcabcdefghijkdabcdefghijkeabcdefghijkfabcdefghijkgabcdefghijkhabcdefghijkiabcdefghijkjabcdefghijkkabcdefghijkaabcdefghijklbabcdefghijklcabcdefghijkldabcdefghijkleabcdefghijklfabcdefghijklgabcdefghijklhabcdefghijkliabcdefghijkljabcdefghijklkabcdefghijkllabcdefghijklaabcdefghijklmbabcdefghijklmcabcdefghijklmdabcdefghijklmeabcdefghijklmfabcdefghijklmgabcdefghijklmhabcdefghijklmiabcdefghijklmjabcdefghijklmkabcdefghijklmlabcdefghijklmmabcdefghijklmaabcdefghijklmnbabcdefghijklmncabcdefghijklmndabcdefghijklmneabcdefghijklmnfabcdefghijklmngabcdefghijklmnhabcdefghijklmniabcdefghijklmnjabcdefghijklmnkabcdefghijklmnlabcdefghijklmnmabcdefghijklmnnabcdefghijklmnaabcdefghijklmnobabcdefghijklmnocabcdefghijklmnodabcdefghijklmnoeabcdefghijklmnofabcdefghijklmnogabcdefghijklmnohabcdefghijklmnoiabcdefghijklmnojabcdefghijklmnokabcdefghijklmnolabcdefghijklmnomabcdefghijklmnonabcdefghijklmnooabcdefghijklmnoaabcdefghijklmnopbabcdefghijklmnopcabcdefghijklmnopdabcdefghijklmnopeabcdefghijklmnopfabcdefghijklmnopgabcdefghijklmnophabcdefghijklmnopiabcdefghijklmnopjabcdefghijklmnopkabcdefghijklmnoplabcdefghijklmnopmabcdefghijklmnopnabcdefghijklmnopoabcdefghijklmnoppabcdefghijklmnopaabcdefghijklmnopqbabcdefghijklmnopqcabcdefghijklmnopqdabcdefghijklmnopqeabcdefghijklmnopqfabcdefghijklmnopqgabcdefghijklmnopqhabcdefghijklmnopqiabcdefghijklmnopqjabcdefghijklmnopqkabcdefghijklmnopqlabcdefghijklmnopqmabcdefghijklmnopqnabcdefghijklmnopqoabcdefghijklmnopqpabcdefghijklmnopqqabcdefghijklmnopqaabcdefghijklmnopqrbabcdefghijklmnopqrcabcdefghijklmnopqrdabcdefghijklmnopqreabcdefghijklmnopqrfabcdefghijklmnopqrgabcdefghijklmnopqrhabcdefghijklmnopqriabcdefghijklmnopqrjabcdefghijklmnopqrkabcdefghijklmnopqrlabcdefghijklmnopqrmabcdefghijklmnopqrnabcdefghijklmnopqroabcdefghijklmnopqrpabcdefghijklmnopqrqabcdefghijklmnopqrrabcdefghijklmnopqraabcdefghijklmnopqrsbabcdefghijklmnopqrscabcdefghijklmnopqrsdabcdefghijklmnopqrseabcdefghijklmnopqrsfabcdefghijklmnopqrsgabcdefghijklmnopqrshabcdefghijklmnopqrsiabcdefghijklmnopqrsjabcdefghijklmnopqrskabcdefghijklmnopqrslabcdefghijklmnopqrsmabcdefghijklmnopqrsnabcdefghijklmnopqrsoabcdefghijklmnopqrspabcdefghijklmnopqrsqabcdefghijklmnopqrsrabcdefghijklmnopqrssabcdefghijklmnopqrsaabcdefghijklmnopqrstbabcdefghijklmnopqrstcabcdefghijklmnopqrstdabcdefghijklmnopqrsteabcdefghijklmnopqrstfabcdefghijklmnopqrstgabcdefghijklmnopqrsthabcdefghijklmnopqrstiabcdefghijklmnopqrstjabcdefghijklmnopqrstkabcdefghijklmnopqrstlabcdefghijklmnopqrstmabcdefghijklmnopqrstnabcdefghijklmnopqrstoabcdefghijklmnopqrstpabcdefghijklmnopqrstqabcdefghijklmnopqrstrabcdefghijklmnopqrstsabcdefghijklmnopqrsttabcdefghijklmnopqrstaabcdefghijklmnopqrstubabcdefghijklmnopqrstucabcdefghijklmnopqrstudabcdefghijklmnopqrstueabcdefghijklmnopqrstufabcdefghijklmnopqrstugabcdefghijklmnopqrstuhabcdefghijklmnopqrstuiabcdefghijklmnopqrstujabcdefghijklmnopqrstukabcdefghijklmnopqrstulabcdefghijklmnopqrstumabcdefghijklmnopqrstunabcdefghijklmnopqrstuoabcdefghijklmnopqrstupabcdefghijklmnopqrstuqabcdefghijklmnopqrsturabcdefghijklmnopqrstusabcdefghijklmnopqrstutabcdefghijklmnopqrstuuabcdefghijklmnopqrstuaabcdefghijklmnopqrstuvbabcdefghijklmnopqrstuvcabcdefghijklmnopqrstuvdabcdefghijklmnopqrstuveabcdefghijklmnopqrstuvfabcdefghijklmnopqrstuvgabcdefghijklmnopqrstuvhabcdefghijklmnopqrstuviabcdefghijklmnopqrstuvjabcdefghijklmnopqrstuvkabcdefghijklmnopqrstuvlabcdefghijklmnopqrstuvmabcdefghijklmnopqrstuvnabcdefghijklmnopqrstuvoabcdefghijklmnopqrstuvpabcdefghijklmnopqrstuvqabcdefghijklmnopqrstuvrabcdefghijklmnopqrstuvsabcdefghijklmnopqrstuvtabcdefghijklmnopqrstuvuabcdefghijklmnopqrstuvvabcdefghijklmnopqrstuvaabcdefghijklmnopqrstuvwbabcdefghijklmnopqrstuvwcabcdefghijklmnopqrstuvwdabcdefghijklmnopqrstuvweabcdefghijklmnopqrstuvwfabcdefghijklmnopqrstuvwgabcdefghijklmnopqrstuvwhabcdefghijklmnopqrstuvwiabcdefghijklmnopqrstuvwjabcdefghijklmnopqrstuvwkabcdefghijklmnopqrstuvwlabcdefghijklmnopqrstuvwmabcdefghijklmnopqrstuvwnabcdefghijklmnopqrstuvwoabcdefghijklmnopqrstuvwpabcdefghijklmnopqrstuvwqabcdefghijklmnopqrstuvwrabcdefghijklmnopqrstuvwsabcdefghijklmnopqrstuvwtabcdefghijklmnopqrstuvwuabcdefghijklmnopqrstuvwvabcdefghijklmnopqrstuvwwabcdefghijklmnopqrstuvwaabcdefghijklmnopqrstuvwxbabcdefghijklmnopqrstuvwxcabcdefghijklmnopqrstuvwxdabcdefghijklmnopqrstuvwxeabcdefghijklmnopqrstuvwxfabcdefghijklmnopqrstuvwxgabcdefghijklmnopqrstuvwxhabcdefghijklmnopqrstuvwxiabcdefghijklmnopqrstuvwxjabcdefghijklmnopqrstuvwxkabcdefghijklmnopqrstuvwxlabcdefghijklmnopqrstuvwxmabcdefghijklmnopqrstuvwxnabcdefghijklmnopqrstuvwxoabcdefghijklmnopqrstuvwxpabcdefghijklmnopqrstuvwxqabcdefghijklmnopqrstuvwxrabcdefghijklmnopqrstuvwxsabcdefghijklmnopqrstuvwxtabcdefghijklmnopqrstuvwxuabcdefghijklmnopqrstuvwxvabcdefghijklmnopqrstuvwxwabcdefghijklmnopqrstuvwxxabcdefghijklmnopqrstuvwxaabcdefghijklmnopqrstuvwxybabcdefghijklmnopqrstuvwxycabcdefghijklmnopqrstuvwxydabcdefghijklmnopqrstuvwxyeabcdefghijklmnopqrstuvwxyfabcdefghijklmnopqrstuvwxygabcdefghijklmnopqrstuvwxyhabcdefghijklmnopqrstuvwxyiabcdefghijklmnopqrstuvwxyjabcdefghijklmnopqrstuvwxykabcdefghijklmnopqrstuvwxylabcdefghijklmnopqrstuvwxymabcdefghijklmnopqrstuvwxynabcdefghijklmnopqrstuvwxyoabcdefghijklmnopqrstuvwxypabcdefghijklmnopqrstuvwxyqabcdefghijklmnopqrstuvwxyrabcdefghijklmnopqrstuvwxysabcdefghijklmnopqrstuvwxytabcdefghijklmnopqrstuvwxyuabcdefghijklmnopqrstuvwxyvabcdefghijklmnopqrstuvwxywabcdefghijklmnopqrstuvwxyxabcdefghijklmnopqrstuvwxyyabcdefghijklmnopqrstuvwxyaabcdefghijklmnopqrstuvwxyzbabcdefghijklmnopqrstuvwxyzcabcdefghijklmnopqrstuvwxyzdabcdefghijklmnopqrstuvwxyzeabcdefghijklmnopqrstuvwxyzfabcdefghijklmnopqrstuvwxyzgabcdefghijklmnopqrstuvwxyzhabcdefghijklmnopqrstuvwxyziabcdefghijklmnopqrstuvwxyzjabcdefghijklmnopqrstuvwxyzkabcdefghijklmnopqrstuvwxyzlabcdefghijklmnopqrstuvwxyzmabcdefghijklmnopqrstuvwxyznabcdefghijklmnopqrstuvwxyzoabcdefghijklmnopqrstuvwxyzpabcdefghijklmnopqrstuvwxyzqabcdefghijklmnopqrstuvwxyzrabcdefghijklmnopqrstuvwxyzsabcdefghijklmnopqrstuvwxyztabcdefghijklmnopqrstuvwxyzuabcdefghijklmnopqrstuvwxyzvabcdefghijklmnopqrstuvwxyzwabcdefghijklmnopqrstuvwxyzxabcdefghijklmnopqrstuvwxyzyabcdefghijklmnopqrstuvwxyzzabcdefghijklmnopqrstuvwxyz
 -->) | [5131.00](https://codegolf.stackexchange.com/questions/233768] <!-- aaaabbabaabcbabccabcaabcdbabcdcabcddabcdaabcdebabcdecabcdedabcdeeabcdeaabcdefbabcdefcabcdefdabcdefeabcdeffabcdefaabcdefgbabcdefgcabcdefgdabcdefgeabcdefgfabcdefggabcdefgaabcdefghbabcdefghcabcdefghdabcdefgheabcdefghfabcdefghgabcdefghhabcdefghaabcdefghibabcdefghicabcdefghidabcdefghieabcdefghifabcdefghigabcdefghihabcdefghiiabcdefghiaabcdefghijbabcdefghijcabcdefghijdabcdefghijeabcdefghijfabcdefghijgabcdefghijhabcdefghijiabcdefghijjabcdefghijaabcdefghijkbabcdefghijkcabcdefghijkdabcdefghijkeabcdefghijkfabcdefghijkgabcdefghijkhabcdefghijkiabcdefghijkjabcdefghijkkabcdefghijkaabcdefghijklbabcdefghijklcabcdefghijkldabcdefghijkleabcdefghijklfabcdefghijklgabcdefghijklhabcdefghijkliabcdefghijkljabcdefghijklkabcdefghijkllabcdefghijklaabcdefghijklmbabcdefghijklmcabcdefghijklmdabcdefghijklmeabcdefghijklmfabcdefghijklmgabcdefghijklmhabcdefghijklmiabcdefghijklmjabcdefghijklmkabcdefghijklmlabcdefghijklmmabcdefghijklmaabcdefghijklmnbabcdefghijklmncabcdefghijklmndabcdefghijklmneabcdefghijklmnfabcdefghijklmngabcdefghijklmnhabcdefghijklmniabcdefghijklmnjabcdefghijklmnkabcdefghijklmnlabcdefghijklmnmabcdefghijklmnnabcdefghijklmnaabcdefghijklmnobabcdefghijklmnocabcdefghijklmnodabcdefghijklmnoeabcdefghijklmnofabcdefghijklmnogabcdefghijklmnohabcdefghijklmnoiabcdefghijklmnojabcdefghijklmnokabcdefghijklmnolabcdefghijklmnomabcdefghijklmnonabcdefghijklmnooabcdefghijklmnoaabcdefghijklmnopbabcdefghijklmnopcabcdefghijklmnopdabcdefghijklmnopeabcdefghijklmnopfabcdefghijklmnopgabcdefghijklmnophabcdefghijklmnopiabcdefghijklmnopjabcdefghijklmnopkabcdefghijklmnoplabcdefghijklmnopmabcdefghijklmnopnabcdefghijklmnopoabcdefghijklmnoppabcdefghijklmnopaabcdefghijklmnopqbabcdefghijklmnopqcabcdefghijklmnopqdabcdefghijklmnopqeabcdefghijklmnopqfabcdefghijklmnopqgabcdefghijklmnopqhabcdefghijklmnopqiabcdefghijklmnopqjabcdefghijklmnopqkabcdefghijklmnopqlabcdefghijklmnopqmabcdefghijklmnopqnabcdefghijklmnopqoabcdefghijklmnopqpabcdefghijklmnopqqabcdefghijklmnopqaabcdefghijklmnopqrbabcdefghijklmnopqrcabcdefghijklmnopqrdabcdefghijklmnopqreabcdefghijklmnopqrfabcdefghijklmnopqrgabcdefghijklmnopqrhabcdefghijklmnopqriabcdefghijklmnopqrjabcdefghijklmnopqrkabcdefghijklmnopqrlabcdefghijklmnopqrmabcdefghijklmnopqrnabcdefghijklmnopqroabcdefghijklmnopqrpabcdefghijklmnopqrqabcdefghijklmnopqrrabcdefghijklmnopqraabcdefghijklmnopqrsbabcdefghijklmnopqrscabcdefghijklmnopqrsdabcdefghijklmnopqrseabcdefghijklmnopqrsfabcdefghijklmnopqrsgabcdefghijklmnopqrshabcdefghijklmnopqrsiabcdefghijklmnopqrsjabcdefghijklmnopqrskabcdefghijklmnopqrslabcdefghijklmnopqrsmabcdefghijklmnopqrsnabcdefghijklmnopqrsoabcdefghijklmnopqrspabcdefghijklmnopqrsqabcdefghijklmnopqrsrabcdefghijklmnopqrssabcdefghijklmnopqrsaabcdefghijklmnopqrstbabcdefghijklmnopqrstcabcdefghijklmnopqrstdabcdefghijklmnopqrsteabcdefghijklmnopqrstfabcdefghijklmnopqrstgabcdefghijklmnopqrsthabcdefghijklmnopqrstiabcdefghijklmnopqrstjabcdefghijklmnopqrstkabcdefghijklmnopqrstlabcdefghijklmnopqrstmabcdefghijklmnopqrstnabcdefghijklmnopqrstoabcdefghijklmnopqrstpabcdefghijklmnopqrstqabcdefghijklmnopqrstrabcdefghijklmnopqrstsabcdefghijklmnopqrsttabcdefghijklmnopqrstaabcdefghijklmnopqrstubabcdefghijklmnopqrstucabcdefghijklmnopqrstudabcdefghijklmnopqrstueabcdefghijklmnopqrstufabcdefghijklmnopqrstugabcdefghijklmnopqrstuhabcdefghijklmnopqrstuiabcdefghijklmnopqrstujabcdefghijklmnopqrstukabcdefghijklmnopqrstulabcdefghijklmnopqrstumabcdefghijklmnopqrstunabcdefghijklmnopqrstuoabcdefghijklmnopqrstupabcdefghijklmnopqrstuqabcdefghijklmnopqrsturabcdefghijklmnopqrstusabcdefghijklmnopqrstutabcdefghijklmnopqrstuuabcdefghijklmnopqrstuaabcdefghijklmnopqrstuvbabcdefghijklmnopqrstuvcabcdefghijklmnopqrstuvdabcdefghijklmnopqrstuveabcdefghijklmnopqrstuvfabcdefghijklmnopqrstuvgabcdefghijklmnopqrstuvhabcdefghijklmnopqrstuviabcdefghijklmnopqrstuvjabcdefghijklmnopqrstuvkabcdefghijklmnopqrstuvlabcdefghijklmnopqrstuvmabcdefghijklmnopqrstuvnabcdefghijklmnopqrstuvoabcdefghijklmnopqrstuvpabcdefghijklmnopqrstuvqabcdefghijklmnopqrstuvrabcdefghijklmnopqrstuvsabcdefghijklmnopqrstuvtabcdefghijklmnopqrstuvuabcdefghijklmnopqrstuvvabcdefghijklmnopqrstuvaabcdefghijklmnopqrstuvwbabcdefghijklmnopqrstuvwcabcdefghijklmnopqrstuvwdabcdefghijklmnopqrstuvweabcdefghijklmnopqrstuvwfabcdefghijklmnopqrstuvwgabcdefghijklmnopqrstuvwhabcdefghijklmnopqrstuvwiabcdefghijklmnopqrstuvwjabcdefghijklmnopqrstuvwkabcdefghijklmnopqrstuvwlabcdefghijklmnopqrstuvwmabcdefghijklmnopqrstuvwnabcdefghijklmnopqrstuvwoabcdefghijklmnopqrstuvwpabcdefghijklmnopqrstuvwqabcdefghijklmnopqrstuvwrabcdefghijklmnopqrstuvwsabcdefghijklmnopqrstuvwtabcdefghijklmnopqrstuvwuabcdefghijklmnopqrstuvwvabcdefghijklmnopqrstuvwwabcdefghijklmnopqrstuvwaabcdefghijklmnopqrstuvwxbabcdefghijklmnopqrstuvwxcabcdefghijklmnopqrstuvwxdabcdefghijklmnopqrstuvwxeabcdefghijklmnopqrstuvwxfabcdefghijklmnopqrstuvwxgabcdefghijklmnopqrstuvwxhabcdefghijklmnopqrstuvwxiabcdefghijklmnopqrstuvwxjabcdefghijklmnopqrstuvwxkabcdefghijklmnopqrstuvwxlabcdefghijklmnopqrstuvwxmabcdefghijklmnopqrstuvwxnabcdefghijklmnopqrstuvwxoabcdefghijklmnopqrstuvwxpabcdefghijklmnopqrstuvwxqabcdefghijklmnopqrstuvwxrabcdefghijklmnopqrstuvwxsabcdefghijklmnopqrstuvwxtabcdefghijklmnopqrstuvwxuabcdefghijklmnopqrstuvwxvabcdefghijklmnopqrstuvwxwabcdefghijklmnopqrstuvwxxabcdefghijklmnopqrstuvwxaabcdefghijklmnopqrstuvwxybabcdefghijklmnopqrstuvwxycabcdefghijklmnopqrstuvwxydabcdefghijklmnopqrstuvwxyeabcdefghijklmnopqrstuvwxyfabcdefghijklmnopqrstuvwxygabcdefghijklmnopqrstuvwxyhabcdefghijklmnopqrstuvwxyiabcdefghijklmnopqrstuvwxyjabcdefghijklmnopqrstuvwxykabcdefghijklmnopqrstuvwxylabcdefghijklmnopqrstuvwxymabcdefghijklmnopqrstuvwxynabcdefghijklmnopqrstuvwxyoabcdefghijklmnopqrstuvwxypabcdefghijklmnopqrstuvwxyqabcdefghijklmnopqrstuvwxyrabcdefghijklmnopqrstuvwxysabcdefghijklmnopqrstuvwxytabcdefghijklmnopqrstuvwxyuabcdefghijklmnopqrstuvwxyvabcdefghijklmnopqrstuvwxywabcdefghijklmnopqrstuvwxyxabcdefghijklmnopqrstuvwxyyabcdefghijklmnopqrstuvwxyaabcdefghijklmnopqrstuvwxyzbabcdefghijklmnopqrstuvwxyzcabcdefghijklmnopqrstuvwxyzdabcdefghijklmnopqrstuvwxyzeabcdefghijklmnopqrstuvwxyzfabcdefghijklmnopqrstuvwxyzgabcdefghijklmnopqrstuvwxyzhabcdefghijklmnopqrstuvwxyziabcdefghijklmnopqrstuvwxyzjabcdefghijklmnopqrstuvwxyzkabcdefghijklmnopqrstuvwxyzlabcdefghijklmnopqrstuvwxyzmabcdefghijklmnopqrstuvwxyznabcdefghijklmnopqrstuvwxyzoabcdefghijklmnopqrstuvwxyzpabcdefghijklmnopqrstuvwxyzqabcdefghijklmnopqrstuvwxyzrabcdefghijklmnopqrstuvwxyzsabcdefghijklmnopqrstuvwxyztabcdefghijklmnopqrstuvwxyzuabcdefghijklmnopqrstuvwxyzvabcdefghijklmnopqrstuvwxyzwabcdefghijklmnopqrstuvwxyzxabcdefghijklmnopqrstuvwxyzyabcdefghijklmnopqrstuvwxyzzabcdefghijklmnopqrstuvwxyz
 -->) | [37.00](https://codegolf.stackexchange.com/questions/226832] <!-- »⌐ṫżṫṗƛ&%≠ɽ_~ẇ*⁼3L ≈;n~U7⋏₇ḭǔ°₁>Aµ1I(□]:ȯ≤KWƒʁY•₇⟩-RCa⟨&8ẋżṫẏL_ġN⇧ṗḞΠṄẇ%¨ḃ₆Q<Zǒ,]„∨TC⁋⟩`ɾOn^≬İ¾¨Ṫlṅ^£†i-ẏ₂↓∷×ṘǍ¶G?∑x∪ż∪İɖ¹p*₴Ḣ≈J₀↳₁‡x⌈↳D4xJḢmḃẇDpeH&⋏¹!≥₇∑;↑≬m†¥⁋†₇,Ż∪ß^ċ¡}GBİ£:U~ʁ⌈∴Ṡ^ṗ⁺Ȯo↓Ṅ%Ẏṗ§∴ḭ₈Ṁ‛∑ø≈dOƒ¥¤ɖ4Ẏ{⅛I∞_uė∇ṫḭB?U≤ǔ9F⟑q₴ẆŀṠz∞₁XṖ¨‛₇VB₁τḟAsżǒxP∵9)&∵β"Ż∆ ↲,₴øxJT.t꘍/₴ǎpe↔ḟqȯ(^≥Vḭ⁰Ȯɽτ∆ṙ°÷lW≠⇧Cb≠²∩]±ḭy∧D℅øJǔ₅⅛EGḭ≥ẋZ≥×8nΠḋ⟩)Ṗv‹'⇧@jq≥ḟ⁽]¾fǎ⅛Ȯ⌊bDa^ṀP;}ṫ⁼τ1„√ɽh⇩GW€⁼[6¼U~j_IṘ†gJ↔Ȧ$°§_„)Ż"₅‡xußġ₃ǔ↔×ɖɖ[æ¥s‹⁰≈c†t‹ṪṙḊ꘍bεβ¶∩∩{ǒḢġ†₅⟨L⌐∨H»`! `τ75ẇ
 -->) | [2.00](https://codegolf.stackexchange.com/questions/231288] <!-- → -->) |
| min mode | [6.00](https://codegolf.stackexchange.com/questions/253739] <!-- vΠ₆↳›
 -->) | [5.00](https://codegolf.stackexchange.com/questions/253720] <!-- λvxΠ›
 -->) | [-1.00](https://codegolf.stackexchange.com/questions/253794] <!-- ɾ:∑p²ƒ-
 -->) | [1.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) |
| max mode | [6.00](https://codegolf.stackexchange.com/questions/253739] <!-- vΠ₆↳›
 -->) | [5.00](https://codegolf.stackexchange.com/questions/253720] <!-- λvxΠ›
 -->) | [-1.00](https://codegolf.stackexchange.com/questions/253794] <!-- ɾ:∑p²ƒ-
 -->) | [1.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) |

## Short programs (length < 10)

| N=906 | Original |  Compressed | Difference | Ratio |
| -- | -- | -- | -- | -- |
| mean | [5.67](https://codegolf.stackexchange.com/questions/253830] <!-- h\d=[1p|]⁽±Ḋ→a⟨←aL5=|←a⌊±T⟨0|2|4⟩=|←a1i\d=|←a3i\+=⟩A[←a0i⌊ʁ(←a2i⌊℅⅛)¾∑←a4i⌊+,|«¢q⁰∷Ṗ-←¥«,
 -->) | [5.17](https://codegolf.stackexchange.com/questions/253771] <!-- O≤[Ẇy?NẎY|_
 -->) | [-0.49](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [0.91](https://codegolf.stackexchange.com/questions/253739] <!-- vΠ₆↳›
 -->) |
| stdev | [2.20](https://codegolf.stackexchange.com/questions/253375] <!-- CÞǔ0€∩L
 -->) | [2.13](https://codegolf.stackexchange.com/questions/253395] <!-- `IṘ`IṘ
 -->) | [0.54](https://codegolf.stackexchange.com/questions/250144] <!-- ṡ
 -->) | [0.13](https://codegolf.stackexchange.com/questions/246504] <!-- b∑
 -->) |
| min | [0.00](https://codegolf.stackexchange.com/questions/246504] <!-- b∑
 -->) | [0.00](https://codegolf.stackexchange.com/questions/246504] <!-- b∑
 -->) | [-2.00](https://codegolf.stackexchange.com/questions/253490] <!-- ÞRs¯0p
 -->) | [0.00](https://codegolf.stackexchange.com/questions/246504] <!-- b∑
 -->) |
| 10% med | [3.00](https://codegolf.stackexchange.com/questions/253476] <!-- 0ṡṅL
 -->) | [2.00](https://codegolf.stackexchange.com/questions/253395] <!-- `IṘ`IṘ
 -->) | [-1.00](https://codegolf.stackexchange.com/questions/248543] <!-- k2T0ẋ→_0→0?£{D¥L<|¥i:‛+-$c[:‛ +ḟ←_:_←›Ǔṫ∇∇+J←›ǔ→_|:‛<>$c[:‛ >ḟ←+→|:\.=[←_← iC₴|:\,=[←_:_←?CȦ→_|:\[=[←_← i¬[Ȯ¥$ȯ\]ḟ∇∇+$]|:\]=[Ȯ¥$Ẏf\[=TG‹∇$_]]]]]]]_›
 -->) | [0.75](https://codegolf.stackexchange.com/questions/253516] <!-- 4(∩ṘǏǔ)3vl3lƛ∩ṠCvṁṙC
 -->) |
| 25% med | [4.00](https://codegolf.stackexchange.com/questions/253730] <!-- fG›β)Ẋ
 -->) | [3.00](https://codegolf.stackexchange.com/questions/253516] <!-- 4(∩ṘǏǔ)3vl3lƛ∩ṠCvṁṙC
 -->) | [-1.00](https://codegolf.stackexchange.com/questions/248543] <!-- k2T0ẋ→_0→0?£{D¥L<|¥i:‛+-$c[:‛ +ḟ←_:_←›Ǔṫ∇∇+J←›ǔ→_|:‛<>$c[:‛ >ḟ←+→|:\.=[←_← iC₴|:\,=[←_:_←?CȦ→_|:\[=[←_← i¬[Ȯ¥$ȯ\]ḟ∇∇+$]|:\]=[Ȯ¥$Ẏf\[=TG‹∇$_]]]]]]]_›
 -->) | [0.83](https://codegolf.stackexchange.com/questions/253771] <!-- O≤[Ẇy?NẎY|_
 -->) |
| median | [6.00](https://codegolf.stackexchange.com/questions/253830] <!-- h\d=[1p|]⁽±Ḋ→a⟨←aL5=|←a⌊±T⟨0|2|4⟩=|←a1i\d=|←a3i\+=⟩A[←a0i⌊ʁ(←a2i⌊℅⅛)¾∑←a4i⌊+,|«¢q⁰∷Ṗ-←¥«,
 -->) | [5.00](https://codegolf.stackexchange.com/questions/253771] <!-- O≤[Ẇy?NẎY|_
 -->) | [0.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [1.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) |
| 75% med | [8.00](https://codegolf.stackexchange.com/questions/248543] <!-- k2T0ẋ→_0→0?£{D¥L<|¥i:‛+-$c[:‛ +ḟ←_:_←›Ǔṫ∇∇+J←›ǔ→_|:‛<>$c[:‛ >ḟ←+→|:\.=[←_← iC₴|:\,=[←_:_←?CȦ→_|:\[=[←_← i¬[Ȯ¥$ȯ\]ḟ∇∇+$]|:\]=[Ȯ¥$Ẏf\[=TG‹∇$_]]]]]]]_›
 -->) | [7.00](https://codegolf.stackexchange.com/questions/248543] <!-- k2T0ẋ→_0→0?£{D¥L<|¥i:‛+-$c[:‛ +ḟ←_:_←›Ǔṫ∇∇+J←›ǔ→_|:‛<>$c[:‛ >ḟ←+→|:\.=[←_← iC₴|:\,=[←_:_←?CȦ→_|:\[=[←_← i¬[Ȯ¥$ȯ\]ḟ∇∇+$]|:\]=[Ȯ¥$Ẏf\[=TG‹∇$_]]]]]]]_›
 -->) | [0.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [1.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) |
| 90% med | [9.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [8.00](https://codegolf.stackexchange.com/questions/253739] <!-- vΠ₆↳›
 -->) | [0.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [1.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) |
| max | [9.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [9.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [1.00](https://codegolf.stackexchange.com/questions/250144] <!-- ṡ
 -->) | [2.00](https://codegolf.stackexchange.com/questions/246188] <!-- ƛƛ⁰O;g
 -->) |
| min mode | [6.00](https://codegolf.stackexchange.com/questions/253830] <!-- h\d=[1p|]⁽±Ḋ→a⟨←aL5=|←a⌊±T⟨0|2|4⟩=|←a1i\d=|←a3i\+=⟩A[←a0i⌊ʁ(←a2i⌊℅⅛)¾∑←a4i⌊+,|«¢q⁰∷Ṗ-←¥«,
 -->) | [5.00](https://codegolf.stackexchange.com/questions/253771] <!-- O≤[Ẇy?NẎY|_
 -->) | [0.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [1.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) |
| max mode | [6.00](https://codegolf.stackexchange.com/questions/253830] <!-- h\d=[1p|]⁽±Ḋ→a⟨←aL5=|←a⌊±T⟨0|2|4⟩=|←a1i\d=|←a3i\+=⟩A[←a0i⌊ʁ(←a2i⌊℅⅛)¾∑←a4i⌊+,|«¢q⁰∷Ṗ-←¥«,
 -->) | [5.00](https://codegolf.stackexchange.com/questions/253771] <!-- O≤[Ẇy?NẎY|_
 -->) | [0.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [1.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) |

## Medium programs (10 <= length < 100)

| N=843 | Original |  Compressed | Difference | Ratio |
| -- | -- | -- | -- | -- |
| mean | [25.17](https://codegolf.stackexchange.com/questions/253131] <!-- `"λŀ λƈ `*‛⇧Ṫ⇧+` λ¬ I'm λ₅"`?*+ḢṪ
 -->) | [23.29](https://codegolf.stackexchange.com/questions/253316] <!-- ₌ɾ²›↔'2l?:Ẋ⊍¬;h
 -->) | [-1.88](https://codegolf.stackexchange.com/questions/253810] <!-- ⁽Tẇ∑N₀%J
 -->) | [0.92](https://codegolf.stackexchange.com/questions/243926] <!-- »ε¥»₄τ2?»øƒ≈»₇τẋṀf`|^/\.`τ\_+§
 -->) |
| stdev | [18.78](https://codegolf.stackexchange.com/questions/253395] <!-- `IṘ`IṘ
 -->) | [17.58](https://codegolf.stackexchange.com/questions/253395] <!-- `IṘ`IṘ
 -->) | [2.65](https://codegolf.stackexchange.com/questions/251234] <!-- Þż
 -->) | [0.06](https://codegolf.stackexchange.com/questions/248682] <!-- """
!+._\PC\DC-\CC\CC- [|,]#`"""
''' TT__D++,q'''
print(ord("P")-ord("D"))
'''
...{}   ({}+{}+{}+{})*({}+{}+{})
''' 
 -->) |
| min | [10.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [8.00](https://codegolf.stackexchange.com/questions/253313] <!-- Þ∞:ẇ2Ḟ2vḞf
 -->) | [-25.00](https://codegolf.stackexchange.com/questions/248682] <!-- """
!+._\PC\DC-\CC\CC- [|,]#`"""
''' TT__D++,q'''
print(ord("P")-ord("D"))
'''
...{}   ({}+{}+{}+{})*({}+{}+{})
''' 
 -->) | [0.69](https://codegolf.stackexchange.com/questions/248682] <!-- """
!+._\PC\DC-\CC\CC- [|,]#`"""
''' TT__D++,q'''
print(ord("P")-ord("D"))
'''
...{}   ({}+{}+{}+{})*({}+{}+{})
''' 
 -->) |
| 10% med | [10.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [10.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [-4.00](https://codegolf.stackexchange.com/questions/248543] <!-- k2T0ẋ→_0→0?£{D¥L<|¥i:‛+-$c[:‛ +ḟ←_:_←›Ǔṫ∇∇+J←›ǔ→_|:‛<>$c[:‛ >ḟ←+→|:\.=[←_← iC₴|:\,=[←_:_←?CȦ→_|:\[=[←_← i¬[Ȯ¥$ȯ\]ḟ∇∇+$]|:\]=[Ȯ¥$Ẏf\[=TG‹∇$_]]]]]]]_›
 -->) | [0.85](https://codegolf.stackexchange.com/questions/253496] <!-- W?(p:ḣḟ›
 -->) |
| 25% med | [13.00](https://codegolf.stackexchange.com/questions/253771] <!-- O≤[Ẇy?NẎY|_
 -->) | [12.00](https://codegolf.stackexchange.com/questions/253830] <!-- h\d=[1p|]⁽±Ḋ→a⟨←aL5=|←a⌊±T⟨0|2|4⟩=|←a1i\d=|←a3i\+=⟩A[←a0i⌊ʁ(←a2i⌊℅⅛)¾∑←a4i⌊+,|«¢q⁰∷Ṗ-←¥«,
 -->) | [-2.00](https://codegolf.stackexchange.com/questions/253810] <!-- ⁽Tẇ∑N₀%J
 -->) | [0.89](https://codegolf.stackexchange.com/questions/253325] <!-- vtCƒ-19+ǒ‹
 -->) |
| median | [18.00](https://codegolf.stackexchange.com/questions/253158] <!-- `Hλ½ K≥τ⇧¨ Hλ½ K≥τ⇧¨
K≥τ⇧¨ K≥τ⇧¨ Hλ½ Hλ½
Hλ½ R□• Hλ½ R□•
R□• R□• Hλ½ Hλ½`
 -->) | [16.00](https://codegolf.stackexchange.com/questions/253432] <!-- ¯ꜝL
 -->) | [-1.00](https://codegolf.stackexchange.com/questions/253771] <!-- O≤[Ẇy?NẎY|_
 -->) | [0.92](https://codegolf.stackexchange.com/questions/252050] <!-- 4ÞNÞ∞d‹/¦i
 -->) |
| 75% med | [30.00](https://codegolf.stackexchange.com/questions/248435] <!-- ≬bøṖ'ĠÞgḢ;ȯ
 -->) | [28.00](https://codegolf.stackexchange.com/questions/253426] <!-- 3ȯ`HiΠ, I'm ₴ŀ!
 -->) | [-1.00](https://codegolf.stackexchange.com/questions/253771] <!-- O≤[Ẇy?NẎY|_
 -->) | [0.96](https://codegolf.stackexchange.com/questions/253316] <!-- ₌ɾ²›↔'2l?:Ẋ⊍¬;h
 -->) |
| 90% med | [52.60](https://codegolf.stackexchange.com/questions/246510] <!-- bṘB²
 -->) | [49.00](https://codegolf.stackexchange.com/questions/252010] <!-- d$ƈ
 -->) | [0.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [1.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) |
| max | [99.00](https://codegolf.stackexchange.com/questions/248999] <!-- '?+½?↔₃
 -->) | [97.00](https://codegolf.stackexchange.com/questions/248867] <!-- 0?(ṘnEn›ẋJ)E1vẋ0ÞṪṘ∩
 -->) | [7.00](https://codegolf.stackexchange.com/questions/241593] <!-- żƛ{D?L<|?i+1$}!⇩
 -->) | [1.18](https://codegolf.stackexchange.com/questions/247353] <!-- ƛ?=T¯‹≤A;A
 -->) |
| min mode | [10.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [10.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [-1.00](https://codegolf.stackexchange.com/questions/253771] <!-- O≤[Ẇy?NẎY|_
 -->) | [1.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) |
| max mode | [10.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [10.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) | [-1.00](https://codegolf.stackexchange.com/questions/253771] <!-- O≤[Ẇy?NẎY|_
 -->) | [1.00](https://codegolf.stackexchange.com/questions/251056] <!-- SṖ'Ṙ⌊=)ȯt
 -->) |

## Long programs (100 <= length)

| N=82 | Original |  Compressed | Difference | Ratio |
| -- | -- | -- | -- | -- |
| mean | [373.39](https://codegolf.stackexchange.com/questions/253198] <!-- 1u0W2↔Ṫ
 -->) | [289.45](https://codegolf.stackexchange.com/questions/253180] <!-- ≬ĠvṪfİL
 -->) | [-83.94](https://codegolf.stackexchange.com/questions/248543] <!-- k2T0ẋ→_0→0?£{D¥L<|¥i:‛+-$c[:‛ +ḟ←_:_←›Ǔṫ∇∇+J←›ǔ→_|:‛<>$c[:‛ >ḟ←+→|:\.=[←_← iC₴|:\,=[←_:_←?CȦ→_|:\[=[←_← i¬[Ȯ¥$ȯ\]ḟ∇∇+$]|:\]=[Ȯ¥$Ẏf\[=TG‹∇$_]]]]]]]_›
 -->) | [0.91](https://codegolf.stackexchange.com/questions/253738] <!-- Ṅ'L5≤næA∧
 -->) |
| stdev | [833.94](https://codegolf.stackexchange.com/questions/253531] <!-- ɾǐvL∷∑…ε
 -->) | [557.59](https://codegolf.stackexchange.com/questions/253338] <!-- $O
 -->) | [433.24](https://codegolf.stackexchange.com/questions/253240] <!-- ÞȮ
 -->) | [0.15](https://codegolf.stackexchange.com/questions/253338] <!-- $O
 -->) |
| min | [102.00](https://codegolf.stackexchange.com/questions/253268] <!-- 9ε:ẏǎ*∑›
 -->) | [77.00](https://codegolf.stackexchange.com/questions/253537] <!-- 'ǐ₂;L~ε"
 -->) | [-3680.00](https://codegolf.stackexchange.com/questions/253338] <!-- $O
 -->) | [0.13](https://codegolf.stackexchange.com/questions/253338] <!-- $O
 -->) |
| 10% med | [117.90](https://codegolf.stackexchange.com/questions/253738] <!-- Ṅ'L5≤næA∧
 -->) | [108.00](https://codegolf.stackexchange.com/questions/253738] <!-- Ṅ'L5≤næA∧
 -->) | [-84.80](https://codegolf.stackexchange.com/questions/253179] <!-- ‛ėġ⇧$F
 -->) | [0.76](https://codegolf.stackexchange.com/questions/253420] <!-- d:√ṙ‹²+‹
 -->) |
| 25% med | [144.00](https://codegolf.stackexchange.com/questions/220138] <!-- `I$O`I$O
 -->) | [128.00](https://codegolf.stackexchange.com/questions/253730] <!-- fG›β)Ẋ
 -->) | [-36.25](https://codegolf.stackexchange.com/questions/253717] <!-- ›"ƛȧ‹*[½₍⌊⌈Uvx∑;÷ȧ"
 -->) | [0.82](https://codegolf.stackexchange.com/questions/253191] <!-- Ġt
 -->) |
| median | [220.00](https://codegolf.stackexchange.com/questions/253395] <!-- `IṘ`IṘ
 -->) | [201.00](https://codegolf.stackexchange.com/questions/253517] <!-- krv↔⁽LġṠÞṡ)Ẋ
 -->) | [-15.00](https://codegolf.stackexchange.com/questions/253154] <!-- kP'Cb∑?=
 -->) | [0.89](https://codegolf.stackexchange.com/questions/253503] <!-- ʀA[⁰øA∑|u
 -->) |
| 75% med | [268.25](https://codegolf.stackexchange.com/questions/253194] <!-- ≠
 -->) | [268.25](https://codegolf.stackexchange.com/questions/253496] <!-- W?(p:ḣḟ›
 -->) | [9.50](https://codegolf.stackexchange.com/questions/253810] <!-- ⁽Tẇ∑N₀%J
 -->) | [1.05](https://codegolf.stackexchange.com/questions/253720] <!-- λvxΠ›
 -->) |
| 90% med | [533.30](https://codegolf.stackexchange.com/questions/253133] <!-- vṄΠ'fs12ɾ⁼
 -->) | [470.40](https://codegolf.stackexchange.com/questions/253240] <!-- ÞȮ
 -->) | [19.00](https://codegolf.stackexchange.com/questions/253432] <!-- ¯ꜝL
 -->) | [1.08](https://codegolf.stackexchange.com/questions/253395] <!-- `IṘ`IṘ
 -->) |
| max | [6553.00](https://codegolf.stackexchange.com/questions/253333] <!-- ɾɾRṅṅ
 -->) | [5131.00](https://codegolf.stackexchange.com/questions/253333] <!-- ɾɾRṅṅ
 -->) | [37.00](https://codegolf.stackexchange.com/questions/253240] <!-- ÞȮ
 -->) | [1.09](https://codegolf.stackexchange.com/questions/253313] <!-- Þ∞:ẇ2Ḟ2vḞf
 -->) |
| min mode | [250.00](https://codegolf.stackexchange.com/questions/253496] <!-- W?(p:ḣḟ›
 -->) | [108.00](https://codegolf.stackexchange.com/questions/253738] <!-- Ṅ'L5≤næA∧
 -->) | [18.00](https://codegolf.stackexchange.com/questions/253720] <!-- λvxΠ›
 -->) | [0.92](https://codegolf.stackexchange.com/questions/253738] <!-- Ṅ'L5≤næA∧
 -->) |
| max mode | [250.00](https://codegolf.stackexchange.com/questions/253496] <!-- W?(p:ḣḟ›
 -->) | [108.00](https://codegolf.stackexchange.com/questions/253738] <!-- Ṅ'L5≤næA∧
 -->) | [18.00](https://codegolf.stackexchange.com/questions/253720] <!-- λvxΠ›
 -->) | [1.07](https://codegolf.stackexchange.com/questions/253496] <!-- W?(p:ḣḟ›
 -->) |
<!-- END AUTOGENERATED TABLE -->

Saves around 4-5 bytes on average (but with huge variability), does nothing most of the time. Occasionally make the program slightly longer. More savings for long programs but still a small average reduction even for very short programs.

# How do I run it?

## Collect your own data

If you want to collect your own data, you will need to set the `STACK_API_KEY` environment variable to your stack apps API key then remove the `if False` from `collect_data.py` and run it.

## Building a tree from the data

This depends on the `code_json.json` file created in the previous step. You could also chose to replace this with your own corpus.

You can then run `analize_data.py` to build a tree.

To visualize the tree you can use the command `dot -Tsvg graph.dot -o out.svg`. It's debatable whether this visualization is helpful.

## Use the data

The `encode_decode.py` will benchmark the encoding and produce the table like seen above. It will also make sure the enccoding is sane.

To use in your own script, use like this:

```py
from vyxμ import encode_decode

forest = encode_decode.load_forest()
encoded_string = encode_decode.bits_to_bytes(encode_decode.encode(string, forest))
```

For decoding use the same except inverse.