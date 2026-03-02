.proc LoadColumn
  php                   ; save registers
  pha
  txa
  pha
  tya
  pha

  lda #%00000100        ; tiles are 32 spaces apart, set PPU to +32 mode
  sta PPUCTRL

  ldy column_number

  lda ColumnLow, y
  sta column_address
  
  lda nametable_number
  eor #$01
  cmp #$00
  bne Nametable1
  lda ColumnHighNT0, y
  sta column_address+1
  jmp DrawColumn
Nametable1:
  lda ColumnHighNT1, y
  sta column_address+1

DrawColumn:

  lda level_data
  clc
  adc #30
  sta level_data
  bcc :+
  inc level_data+1
:

  lda PPUSTATUS
  lda column_address + 1
  sta PPUADDR
  lda column_address
  sta PPUADDR
  ldx #$1E              ; $1E = 30 tiles per column
  ldy #$00
DrawColumnLoop:
  lda (level_data), y
  sta PPUDATA
  iny
  dex
  bne DrawColumnLoop

  pla                   ; restore registers
  tay
  pla
  tax
  pla
  plp

  rts
.endproc