
f <- c(1.197000, 1.330000, 1.463000, 1.596000, 1.729000, 1.862000, 1.995000, 2.128000, 2.261000, 2.394000)
Tamb <- 28.5
R <- 0.3685
a1 <- 0.0061
a2 <- 4.5036
a3 <- 0.0928
a4 <- -0.3536
a5 <- -4.6606
a6 <- 64.8758
#a1 <- 0.0069
#a2 <- 7.3865
#a3 <- 0.0405
#a4 <- -0.4351
#a5 <- -6.9793
#a6 <- 61.1205

A <- a1*R
B <- a3*R*f + a4*R - 1
C <- a2*f^2*R + a5*R + a6*R + Tamb

print(f)

T <- -B/(2*A) - sqrt(B^2 - 4*A*C)/(2*A)
P <- a1*T^2 + a2*f^2 + a3*T*f + a4*T + a5*f + a6

print(T)
print(P)