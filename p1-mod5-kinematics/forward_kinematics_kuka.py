from sympy import symbols, cos, sin, pi, sqrt, simplify
from sympy.matrices import Matrix

q1, q2, q3, q4, q5, q6, q7 = symbols('q1:8')
d1, d2, d3, d4, d5, d6, d7 = symbols('d1:8')
a0, a1, a2, a3, a4, a5, a6 = symbols('a0:7')
alp0, alp1, alp2, alp3, alp4, alp5, alp6 = symbols('alp0:7')

#DH Parameters
s = {alp0:    0, a0:     0, d1: 0.75, 
	alp1:-pi/2, a1:  0.35, d2:    0, q2:q2-pi/2,
	alp2:    0, a2:  1.25, d3:    0, 
	alp3:-pi/2, a3:-0.054, d4:  1.5, 
	alp4: pi/2, a4:     0, d5:    0, 
	alp5:-pi/2, a5:     0, d6:    0, 
	alp6:    0, a6:     0, d7:0.303, q7:0			}

#Transform Matrices
T0_1=Matrix([[cos(q1), -sin(q1), 0, a0], [sin(q1)*cos(alp0), cos(q1)*cos(alp0), -sin(alp0), -sin(alp0)*d1], [sin(q1)*sin(alp0), cos(q1)*sin(alp0), cos(alp0), cos(alp0)*d1], [0, 0, 0, 1]])
T0_1=T0_1.subs(s)

T1_2=Matrix([[cos(q2), -sin(q2), 0, a1], [sin(q2)*cos(alp1), cos(q2)*cos(alp1), -sin(alp1), -sin(alp1)*d2], [sin(q2)*sin(alp1), cos(q2)*sin(alp1), cos(alp1), cos(alp1)*d2], [0, 0, 0, 1]])
T1_2=T1_2.subs(s)

T2_3=Matrix([[cos(q3), -sin(q3), 0, a2], [sin(q3)*cos(alp2), cos(q3)*cos(alp2), -sin(alp2), -sin(alp2)*d3], [sin(q2)*sin(alp2), cos(q3)*sin(alp2), cos(alp2), cos(alp2)*d3], [0, 0, 0, 1]])
T2_3=T2_3.subs(s)

T3_4=Matrix([[cos(q4), -sin(q4), 0, a3], [sin(q4)*cos(alp3), cos(q4)*cos(alp3), -sin(alp3), -sin(alp3)*d4], [sin(q4)*sin(alp3), cos(q4)*sin(alp3), cos(alp3), cos(alp3)*d4], [0, 0, 0, 1]])
T3_4=T3_4.subs(s)

T4_5=Matrix([[cos(q5), -sin(q5), 0, a4], [sin(q5)*cos(alp4), cos(q5)*cos(alp4), -sin(alp4), -sin(alp4)*d5], [sin(q5)*sin(alp4), cos(q5)*sin(alp4), cos(alp4), cos(alp4)*d5], [0, 0, 0, 1]])
T4_5=T4_5.subs(s)

T5_6=Matrix([[cos(q6), -sin(q6), 0, a5], [sin(q6)*cos(alp5), cos(q6)*cos(alp5), -sin(alp5), -sin(alp5)*d6], [sin(q6)*sin(alp5), cos(q6)*sin(alp5), cos(alp5), cos(alp5)*d6], [0, 0, 0, 1]])
T5_6=T5_6.subs(s)

T6_7=Matrix([[cos(q7), -sin(q7), 0, a6], [sin(q7)*cos(alp6), cos(q7)*cos(alp6), -sin(alp6), -sin(alp6)*d7], [sin(q7)*sin(alp6), cos(q7)*sin(alp6), cos(alp6), cos(alp6)*d7], [0, 0, 0, 1]])
T6_7=T6_7.subs(s)

#Composition of Homogenous Transforms
T0_2=simplify(T0_1*T1_2)
T0_3=T0_2*T2_3
T0_4=T0_3*T3_4
T0_5=T0_4*T4_5
T0_6=T0_5*T5_6
T0_7=T0_6*T6_7

#Correction at gripper: One pi rotation about z and then a -pi/2 rotation about y

R_z = Matrix([[cos(pi), -sin(pi), 0, 0], [sin(pi), cos(pi), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
R_y = Matrix([[cos(-pi/2), 0, sin(-pi/2), 0], [0, 1, 0, 0], [-sin(-pi/2), 0, cos(-pi/2), 0], [0, 0, 0, 1]])

R_fin=R_z*R_y

#Intermediate Transforms
print("T0_1= ", T0_1.evalf(subs={q1:0, q2:0, q3:0, q4:0, q5:0, q6:0}))
print("T0_2= ", T0_2.evalf(subs={q1:0, q2:0, q3:0, q4:0, q5:0, q6:0}))
print("T0_3= ", T0_3.evalf(subs={q1:0, q2:0, q3:0, q4:0, q5:0, q6:0}))
print("T0_4= ", T0_4.evalf(subs={q1:0, q2:0, q3:0, q4:0, q5:0, q6:0}))
print("T0_5= ", T0_5.evalf(subs={q1:0, q2:0, q3:0, q4:0, q5:0, q6:0}))
print("T0_6= ", T0_6.evalf(subs={q1:0, q2:0, q3:0, q4:0, q5:0, q6:0}))
print("T0_7= ", T0_7.evalf(subs={q1:0, q2:0, q3:0, q4:0, q5:0, q6:0}))

T0_7=T0_7.evalf(subs={q1:0, q2:0, q3:0, q4:0, q5:0, q6:0})

#Final Homogenous Transform for KUKA
T_fin=T0_7*R_fin
print(T_fin)
