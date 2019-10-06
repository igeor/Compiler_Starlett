	.data
newline: .asciiz "\n"
	.text
L:
	j Lmain
L0:
	#0: begin_block, f3, __, __
	sw $ra, 0($sp) 	# f3
L1:
	#1: +, e, 1, T_1
	lw $t1,-12($sp)
	li $t2,1
	add $t1,$t1,$t2
	sw $t1,-16($sp)
L2:
	lw $t1,-16($sp)
	sw $t1,-12($sp)
	#2: :=, T_1, __, e
L3:
	#3: out, e, __, __
	li $v0,1
	lw $t1,-12($sp)
	move $a0,$t1
	syscall
	li $v0,4
	la $a0,newline
	syscall
L4:
	#4: retv, __, __, e
	lw $t1,-12($sp)
	lw $t0, -8($sp)
	sw $t1,0($t0)
	lw $ra, 0($sp)
	jr $ra
L5:
	#5: end_block, f3, __, __
	lw $ra, 0($sp)
	jr $ra
L6:
	#6: begin_block, f2, __, __
	sw $ra, 0($sp) 	# f2
L7:
	#7: out, y, __, __
	li $v0,1
	lw $t0,-12($sp)
	lw $t1,0($t0)
	move $a0,$t1
	syscall
	li $v0,4
	la $a0,newline
	syscall
L8:
	#8: par, y, cp, __
	addi $fp,$sp,20	#6
	lw $t0,-12($sp)
	lw $t0,0($t0)
	sw $t0,-12($fp) 	#8: par, y, cp, __
L9:
	#9: par, T_2, RET, __
	addi $t0,$sp,-20
	sw $t0,-8($fp)
L10:
	#10: call, f3, __, __
	sw $sp,-4($fp)	#10: call, f3, __, __
	addi $sp,$sp,20
	jal L0
	addi $sp,$sp,-20
	addi $fp,$sp,20
	lw $t0,-12($fp) 	#8: par, y, cp, __#  EDO TO CP
	lw $t0,-12($sp)
	sw $t0,0($t0)

L11:
	lw $t1,-20($sp)
	sw $t1,-16($sp)
	#11: :=, T_2, __, e
L12:
	#12: out, e, __, __
	li $v0,1
	lw $t1,-16($sp)
	move $a0,$t1
	syscall
	li $v0,4
	la $a0,newline
	syscall
L13:
	#13: retv, __, __, e
	lw $t1,-16($sp)
	lw $t0, -8($sp)
	sw $t1,0($t0)
	lw $ra, 0($sp)
	jr $ra
L14:
	#14: end_block, f2, __, __
	lw $ra, 0($sp)
	jr $ra
L15:
	#15: begin_block, f4, __, __
	sw $ra, 0($sp) 	# f4
L16:
	#16: out, x, __, __
	li $v0,1
	lw $t1,-12($sp)
	move $a0,$t1
	syscall
	li $v0,4
	la $a0,newline
	syscall
L17:
	#17: /, x, 2, T_3
	lw $t1,-12($sp)
	li $t2,2
	div $t1,$t1,$t2
	sw $t1,-16($sp)
L18:
	lw $t1,-16($sp)
	sw $t1,-12($sp)
	#18: :=, T_3, __, x
L19:
	#19: out, x, __, __
	li $v0,1
	lw $t1,-12($sp)
	move $a0,$t1
	syscall
	li $v0,4
	la $a0,newline
	syscall
L20:
	#20: retv, __, __, x
	lw $t1,-12($sp)
	lw $t0, -8($sp)
	sw $t1,0($t0)
	lw $ra, 0($sp)
	jr $ra
L21:
	#21: end_block, f4, __, __
	lw $ra, 0($sp)
	jr $ra
L22:
	#22: begin_block, f1, __, __
	sw $ra, 0($sp) 	# f1
L23:
	li $t1,3
	sw $t1,-20($sp)
	#23: :=, 3, __, d
L24:
	#24: out, x, __, __
	li $v0,1
	lw $t1,-12($sp)
	move $a0,$t1
	syscall
	li $v0,4
	la $a0,newline
	syscall
L25:
	#25: par, d, ref, __
	addi $fp,$sp,24	#22
	addi $t0,$sp,-20
	sw $t0,-12($fp) 	#25: par, d, ref, __
L26:
	#26: par, T_4, RET, __
	addi $t0,$sp,-24
	sw $t0,-8($fp)
L27:
	#27: call, f2, __, __
	sw $sp,-4($fp)	#27: call, f2, __, __
	addi $sp,$sp,24
	jal L6
	addi $sp,$sp,-24
L28:
	lw $t1,-24($sp)
	sw $t1,-16($sp)
	#28: :=, T_4, __, c
L29:
	#29: out, c, __, __
	li $v0,1
	lw $t1,-16($sp)
	move $a0,$t1
	syscall
	li $v0,4
	la $a0,newline
	syscall
L30:
	#30: par, c, cv, __
	addi $fp,$sp,20	#22
	lw $t0,-16($sp)
	sw $t0,-12($fp) 	#30: par, c, cv, __
L31:
	#31: par, T_5, RET, __
	addi $t0,$sp,-28
	sw $t0,-8($fp)
L32:
	#32: call, f4, __, __
	sw $sp,-4($fp)	#32: call, f4, __, __
	addi $sp,$sp,20
	jal L15
	addi $sp,$sp,-20
L33:
	lw $t1,-28($sp)
	sw $t1,-16($sp)
	#33: :=, T_5, __, c
L34:
	#34: out, c, __, __
	li $v0,1
	lw $t1,-16($sp)
	move $a0,$t1
	syscall
	li $v0,4
	la $a0,newline
	syscall
L35:
	#35: retv, __, __, c
	lw $t1,-16($sp)
	lw $t0, -8($sp)
	sw $t1,0($t0)
	lw $ra, 0($sp)
	jr $ra
L36:
	#36: end_block, f1, __, __
	lw $ra, 0($sp)
	jr $ra
Lmain:
	addi $sp,$sp,32
	move $s0,$sp
L37:
	#37: begin_block, test1, __, __
	sw $ra, 0($sp) 	# test1
L38:
	#38: -, 0, 1, T_6
	li $t1,0
	li $t2,1
	sub $t1,$t1,$t2
	sw $t1,-20($sp)
L39:
	lw $t1,-20($sp)
	sw $t1,-16($sp)
	#39: :=, T_6, __, b
L40:
	#40: par, b, cv, __
	addi $fp,$sp,32	#37
	lw $t0,-16($sp)
	sw $t0,-12($fp) 	#40: par, b, cv, __
L41:
	#41: par, T_7, RET, __
	addi $t0,$sp,-24
	sw $t0,-8($fp)
L42:
	#42: call, f1, __, __
	sw $sp,-4($fp)	#42: call, f1, __, __
	addi $sp,$sp,32
	jal L22
	addi $sp,$sp,-32
L43:
	#43: -, 0, T_7, T_8
	li $t1,0
	lw $t2,-24($sp)
	sub $t1,$t1,$t2
	sw $t1,-28($sp)
L44:
	lw $t1,-28($sp)
	sw $t1,-12($sp)
	#44: :=, T_8, __, a
L45:
	#45: out, a, __, __
	li $v0,1
	lw $t1,-12($sp)
	move $a0,$t1
	syscall
	li $v0,4
	la $a0,newline
	syscall
L46:
	li $v0, 10
	syscall
L47:
	#47: end_block, test1, __, __
	lw $ra, 0($sp)
	jr $ra
