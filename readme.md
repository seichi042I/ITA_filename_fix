# 概要
**recitation_1**とか**emoA001**など，コーパスの正しいラベルと一致しないファイル名を**RECITATION324_001**，**EMOTION100_001**のように修正する．
コーパス文がそのままファイル名になっている場合には対応していません．
# 使い方
例
```bash
.
├── corpus
│   ├── ITAcorpus_aoba
│   ├── ITAcorpus_ayaka
│   ├── ITAcorpus_giga_rakan
│   ├── ITAcorpus_ginga
│   ├── ITAcorpus_hakutii_deception
│   ├── ITAcorpus_hakutii_desperation
│   ├── ITAcorpus_hakutii_discontent
│   ├── ITAcorpus_hakutii_emaciation
│   ├── ITAcorpus_hakutii_impoverishment
│   ├── ITAcorpus_hakutii_incite
│   ├── ITAcorpus_hakutii_jovially
│   ├── ITAcorpus_hakutii_low
│   ├── ITAcorpus_hakutii_low_whisper
│   ├── ITAcorpus_hakutii_machine
│   ├── ITAcorpus_hakutii_merrily
│   ├── ITAcorpus_hakutii_pleased
│   ├── ITAcorpus_hakutii_refreshing
│   ├── ITAcorpus_hakutii_resignation
│   ├── ITAcorpus_hakutii_tense
│   ├── ITAcorpus_hakutii_whisper
│   ├── ITAcorpus_hakutii_young
│   ├── ITAcorpus_kanon
│   ├── ITAcorpus_kikoto_kurage
│   ├── ITAcorpus_kikoto_mahiro
│   ├── ITAcorpus_kokeiro_kage
│   ├── ITAcorpus_losachan
│   ├── ITAcorpus_matsukaze
│   ├── ITAcorpus_nohoshio
│   ├── ITAcorpus_nohoshio_typeB
│   ├── ITAcorpus_planeta
│   ├── ITAcorpus_runaitoneiru
│   ├── ITAcorpus_takamineito
│   ├── ITAcorpus_tokina_shigure
│   ├── ITAcorpus_ukyo_shiro_normal
│   ├── ITAcorpus_yokune_ruko_f_high
│   ├── ITAcorpus_yokune_ruko_f_low
│   ├── ITAcorpus_yokune_ruko_f_normal
│   ├── ITAcorpus_yokune_ruko_f_whisper
│   ├── ITAemotion_groy_anderson
│   ├── ITAemotion_kuroha_tehu
│   └── ITArecitation_speedspeech
...
```
```bash
python ITA_filename_fix.py $(pwd)/corpus
```
