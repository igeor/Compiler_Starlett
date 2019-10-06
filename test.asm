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
	#15: begin_block, f1, __, __
	sw $ra, 0($sp) 	# f1
L16:
	li $t1,3
	sw $t1,-20($sp)
	#16: :=, 3, __, d
L17:
	#17: out, x, __, __
	li $v0,1
	lw $t1,-12($sp)
	move $a0,$t1
	syscall
	li $v0,4
	la $a0,newline
	syscall
L18:
	#18: par, d, ref, __
	addi $fp,$sp,24	#15
	addi $t0,$sp,-20
	sw $t0,-12($fp) 	#18: par, d, ref, __
L19:
	#19: par, T_3, RET, __
	addi $t0,$sp,-24
	sw $t0,-8($fp)
L20:
	#20: call, f2, __, __
	sw $sp,-4($fp)	#20: call, f2, __, __
	addi $sp,$sp,24
	jal L6
	addi $sp,$sp,-24
L21:
	lw $t1,-24($sp)
	sw $t1,-16($sp)
	#21: :=, T_3, __, c
L22:
	#22: out, c, __, __
	li $v0,1
	lw $t1,-16($sp)
	move $a0,$t1
	syscall
	li $v0,4
	la $a0,newline
	syscall
L23:
	#23: retv, __, __, c
	lw $t1,-16($sp)
	lw $t0, -8($sp)
	sw $t1,0($t0)
	lw $ra, 0($sp)
	jr $ra
L24:
	#24: end_block, f1, __, __
	lw $ra, 0($sp)
	jr $ra
Lmain:
	addi $sp,$sp,32
	move $s0,$sp
L25:
	#25: begin_block, test, __, __
	sw $ra, 0($sp) 	# test
L26:
	#26: -, 0, 1, T_4
	li $t1,0
	li $t2,1
	sub $t1,$t1,$t2
	sw $t1,-20($sp)
L27:
	lw $t1,-20($sp)
	sw $t1,-16($sp)
	#27: :=, T_4, __, b
L28:
	#28: par, b, cv, __
	addi $fp,$sp,28	#25
	lw $t0,-16($sp)
	sw $t0,-12($fp) 	#28: par, b, cv, __
L29:
	#29: par, T_5, RET, __
	addi $t0,$sp,-24
	sw $t0,-8($fp)
L30:
	#30: call, f1, __, __
	sw $sp,-4($fp)	#30: call, f1, __, __
	addi $sp,$sp,28
	jal L15
	addi $sp,$sp,-28
L31:
	#31: -, 0, T_5, T_6
	li $t1,0
	lw $t2,-24($sp)
	sub $t1,$t1,$t2
	sw $t1,-28($sp)
L32:
	lw $t1,-28($sp)
	sw $t1,-12($sp)
	#32: :=, T_6, __, a
L33:
	#33: out, a, __, __
	li $v0,1
	lw $t1,-12($sp)
	move $a0,$t1
	syscall
	li $v0,4
	la $a0,newline
	syscall
L34:
	li $v0, 10
	syscall
L35:
	#35: end_block, test, __, __
	lw $ra, 0($sp)
	jr $ra
