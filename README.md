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
可搭配[網站教學1](https://gaseri.org/en/tutorials/gromacs/1-tip4pew-water/#topology-file)以及[網站教學2](http://dospt.org/index.php/Tutorial_2:_entropy_of_mixing_of_methanol%2Bwater)進行練習

---
## 實用網址
* [Gromacs官網](https://www.gromacs.org/)
* [vmd    官網](https://www.ks.uiuc.edu/Research/vmd/)
* [Gromacs安裝教學](https://zhuanlan.zhihu.com/p/51188872) (註：cmake安裝指令應為 ``cmake .. -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=ON``)
* [Gromacs英文手冊](https://manual.gromacs.org/current/reference-manual/index.html)
* [Gromacs中文手冊](https://jerkwin.github.io/9999/12/31/GROMACS%E4%B8%AD%E6%96%87%E6%89%8B%E5%86%8C/)
* OPLS/AA 資料庫  [LigParGen](http://zarbi.chem.yale.edu/ligpargen/)
* GROMOS96 資料庫 [Automated Topology Builder](https://atb.uq.edu.au/index.py)
* TRAPPE/UA 資料庫 [The Siepmann Group](http://trappe.oit.umn.edu/)
* [系統平衡判斷](http://sobereva.com/627)
