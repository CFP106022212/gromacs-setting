# gromacs-setting
## 運行指令
### Energy minization
gmx grompp -f em.mdp -o min.tpr -pp min.top -po min.mdp -maxwarn 2<br>
gmx mdrun -s min.tpr -deffnm min -v
### NVT
gmx grompp -f NVT.mdp -o eql.tpr -pp eql.top -po eql.mdp -c min.gro -maxwarn 2<br>
gmx mdrun -s eql.tpr -deffnm eql -v
### NPT
gmx grompp -f NPT.mdp -o eql2.tpr -pp eql2.top -po eql2.mdp -c eql.gro -maxwarn 2<br>
gmx mdrun -s eql2.tpr -deffnm eql2 -v
### Production
gmx grompp -f prd.mdp -o prd.tpr -pp prd.top -po prd.mdp -c eql2.gro -maxwarn 2<br>
gmx mdrun -s prd.tpr -deffnm prd -v<br>

---
## 其他範例
可搭配[此網站教學](https://gaseri.org/en/tutorials/gromacs/1-tip4pew-water/#topology-file)進行練習
