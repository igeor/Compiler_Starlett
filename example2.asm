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
	lw $t0,0($t0)
	sw $t1,0($t0)
	#2: :=, w, __, z
L3:
	#3: retv, __, __, e
	lw $t0,-4($sp)
	addi $t0,$t0,-20
	lw $t1,0($t0)
	lw $t0, -8($sp)
	sw $t1,0($t0)
	lw $ra, 0($sp)
	jr $ra
L4:
	#4: end_block, P21, __, __
	lw $ra, 0($sp)
	jr $ra
L5:
	#5: begin_block, P11, __, __
	sw $ra, 0($sp) 	# P11
L6:
	lw $t0,-16($sp)
	lw $t1,0($t0)
	sw $t1,-20($sp)
	#6: :=, z, __, e
L7:
	lw $t1,-12($sp)
	lw $t0,-16($sp)
	sw $t1,0($t0)
	#7: :=, w, __, z
L8:
	#8: par, c, cv, __
	addi $fp,$sp,16	#5
	lw $t0,-4($sp)
	addi $t0,$t0,-20
	lw $t0,0($t0)
	sw $t0,-12($fp) 	#8: par, c, cv, __
L9:
	#9: par, T_1, RET, __
	addi $t0,$sp,-24
	sw $t0,-8($fp)
L10:
	#10: call, P21, __, __
	sw $sp,-4($fp)	#10: call, P21, __, __
	addi $sp,$sp,16
	jal L0
	addi $sp,$sp,-16
L11:
	lw $t1,-24($sp)
	sw $t1,-20($sp)
	#11: :=, T_1, __, e
L12:
	#12: retv, __, __, e
	lw $t1,-20($sp)
	lw $t0, -8($sp)
	sw $t1,0($t0)
	lw $ra, 0($sp)
	jr $ra
L13:
	#13: end_block, P11, __, __
	lw $ra, 0($sp)
	jr $ra
L14:
	#14: begin_block, P1, __, __
	sw $ra, 0($sp) 	# P1
L15:
	li $t1,100
	sw $t1,-16($s0)
	#15: :=, 100, __, b
L16:
	#16: par, b, cv, __
	addi $fp,$sp,28	#14
	lw $t0,-16($s0)
	sw $t0,-12($fp) 	#16: par, b, cv, __
L17:
	#17: par, c, ref, __
	addi $t0,$sp,-20
	sw $t0,-16($fp) 	#17: par, c, ref, __
L18:
	#18: par, T_2, RET, __
	addi $t0,$sp,-28
	sw $t0,-8($fp)
L19:
	#19: call, P11, __, __
	sw $sp,-4($fp)	#19: call, P11, __, __
	addi $sp,$sp,28
	jal L5
	addi $sp,$sp,-28
L20:
	lw $t1,-28($sp)
	sw $t1,-20($sp)
	#20: :=, T_2, __, c
L21:
	#21: +, b, c, T_3
	lw $t1,-16($s0)
	lw $t2,-20($sp)
	add $t1,$t1,$t2
	sw $t1,-32($sp)
L22:
	lw $t1,-32($sp)
	lw $t0,-16($sp)
	sw $t1,0($t0)
	#22: :=, T_3, __, y
L23:
	#23: retv, __, __, y
	lw $t0,-16($sp)
	lw $t1,0($t0)
	lw $t0, -8($sp)
	sw $t1,0($t0)
	lw $ra, 0($sp)
	jr $ra
L24:
	#24: end_block, P1, __, __
	lw $ra, 0($sp)
	jr $ra
Lmain:
	addi $sp,$sp,24
	move $s0,$sp
L25:
	#25: begin_block, example2, __, __
	sw $ra, 0($sp) 	# example2
L26:
	#26: par, a, cv, __
	addi $fp,$sp,36	#25
	lw $t0,-12($sp)
	sw $t0,-12($fp) 	#26: par, a, cv, __
L27:
	#27: par, b, ref, __
	addi $t0,$sp,-16
	sw $t0,-16($fp) 	#27: par, b, ref, __
L28:
	#28: par, T_4, RET, __
	addi $t0,$sp,-20
	sw $t0,-8($fp)
L29:
	#29: call, P1, __, __
	sw $sp,-4($fp)	#29: call, P1, __, __
	addi $sp,$sp,36
	jal L14
	addi $sp,$sp,-36
L30:
	lw $t1,-20($sp)
	sw $t1,-12($sp)
	#30: :=, T_4, __, a
L31:
	li $v0, 10
	syscall
L32:
	#32: end_block, example2, __, __
	lw $ra, 0($sp)
	jr $ra
