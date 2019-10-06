	.data
newline: .asciiz "\n"
	.text
L:
	j Lmain
L0:
	#0: begin_block, P21, __, __
	sw $ra, 0($sp) 	# P21
L1:
	lw $t1,-12($sp)
	lw $t0,-4($sp)
	addi $t0,$t0,-20
	sw $t1,0($t0)
	#1: :=, x, __, e
L2:
	lw $t0,-4($sp)
	addi $t0,$t0,-12
	lw $t1,0($t0)
	lw $t0,-4($sp)
	addi $t0,$t0,-16
	sw $t1,0($t0)
	#2: :=, w, __, z
L3:
	#3: par, a, cv, __
	addi $fp,$sp,20	#0
	lw $t0,-12($s0)
	sw $t0,-12($fp) 	#3: par, a, cv, __
L4:
	#4: par, T_1, RET, __
	addi $t0,$sp,-16
	sw $t0,-8($fp)
L5:
	#5: call, P21, __, __
	lw $t0,-4($sp)	#5: call, P21, __, __
	sw $t0,-4($fp)
	addi $sp,$sp,20
	jal L0
	addi $sp,$sp,-20
L6:
	lw $t1,-16($sp)
	lw $t0,-4($sp)
	addi $t0,$t0,-20
	sw $t1,0($t0)
	#6: :=, T_1, __, e
L7:
	#7: retv, __, __, e
	lw $t0,-4($sp)
	addi $t0,$t0,-20
	lw $t1,0($t0)
	lw $t0, -8($sp)
	sw $t1,0($t0)
	lw $ra, 0($sp)
	jr $ra
L8:
	#8: end_block, P21, __, __
	lw $ra, 0($sp)
	jr $ra
L9:
	#9: begin_block, P11, __, __
	sw $ra, 0($sp) 	# P11
L10:
	lw $t1,-12($sp)
	sw $t1,-16($sp)
	#10: :=, w, __, z
L11:
	#11: par, c, cv, __
	addi $fp,$sp,20	#9
	lw $t0,-4($sp)
	addi $t0,$t0,-20
	lw $t0,0($t0)
	sw $t0,-12($fp) 	#11: par, c, cv, __
L12:
	#12: par, T_2, RET, __
	addi $t0,$sp,-24
	sw $t0,-8($fp)
L13:
	#13: call, P21, __, __
	sw $sp,-4($fp)	#13: call, P21, __, __
	addi $sp,$sp,20
	jal L0
	addi $sp,$sp,-20
L14:
	lw $t1,-24($sp)
	sw $t1,-20($sp)
	#14: :=, T_2, __, e
L15:
	#15: retv, __, __, e
	lw $t1,-20($sp)
	lw $t0, -8($sp)
	sw $t1,0($t0)
	lw $ra, 0($sp)
	jr $ra
L16:
	#16: end_block, P11, __, __
	lw $ra, 0($sp)
	jr $ra
L17:
	#17: begin_block, P1, __, __
	sw $ra, 0($sp) 	# P1
L18:
	li $t1,100
	sw $t1,-16($s0)
	#18: :=, 100, __, b
L19:
	#19: par, b, cp, __
	addi $fp,$sp,28	#17
	lw $t0,-16($s0)
	sw $t0,-12($fp) 	#19: par, b, cp, __
L20:
	#20: par, c, cp, __
	lw $t0,-20($sp)
	sw $t0,-16($fp) 	#20: par, c, cp, __
L21:
	#21: par, T_3, RET, __
	addi $t0,$sp,-28
	sw $t0,-8($fp)
L22:
	#22: call, P11, __, __
	sw $sp,-4($fp)	#22: call, P11, __, __
	addi $sp,$sp,28
	jal L9
	addi $sp,$sp,-28
	addi $fp,$sp,28
	lw $t0,-16($fp) 	#20: par, c, cp, __#  EDO TO CP
	sw $t0,-20($sp)

	lw $t0,-12($fp) 	#19: par, b, cp, __#  EDO TO CP
	sw $t0,-16($s0)

L23:
	lw $t1,-28($sp)
	sw $t1,-20($sp)
	#23: :=, T_3, __, c
L24:
	#24: +, b, c, T_4
	lw $t1,-16($s0)
	lw $t2,-20($sp)
	add $t1,$t1,$t2
	sw $t1,-32($sp)
L25:
	lw $t1,-32($sp)
	sw $t1,-24($s0)
	#25: :=, T_4, __, y
L26:
	#26: retv, __, __, y
	lw $t1,-24($s0)
	lw $t0, -8($sp)
	sw $t1,0($t0)
	lw $ra, 0($sp)
	jr $ra
L27:
	#27: end_block, P1, __, __
	lw $ra, 0($sp)
	jr $ra
Lmain:
	addi $sp,$sp,32
	move $s0,$sp
L28:
	#28: begin_block, example, __, __
	sw $ra, 0($sp) 	# example
L29:
	#29: par, b, cv, __
	addi $fp,$sp,36	#28
	lw $t0,-16($sp)
	sw $t0,-12($fp) 	#29: par, b, cv, __
L30:
	#30: par, c, ref, __
	addi $t0,$sp,-20
	sw $t0,-16($fp) 	#30: par, c, ref, __
L31:
	#31: par, T_5, RET, __
	addi $t0,$sp,-28
	sw $t0,-8($fp)
L32:
	#32: call, P1, __, __
	sw $sp,-4($fp)	#32: call, P1, __, __
	addi $sp,$sp,36
	jal L17
	addi $sp,$sp,-36
L33:
	lw $t1,-28($sp)
	sw $t1,-12($sp)
	#33: :=, T_5, __, a
L34:
	li $v0, 10
	syscall
L35:
	#35: end_block, example, __, __
	lw $ra, 0($sp)
	jr $ra
