# Elstruct Journal Club
Minutes from Journal club meetings for elstruct@LiU

The last meeting was on 2024-09-12.

## Papers discussed in the the last meeting:

1. ### Simultaneously improving accuracy and computational cost under parametric constraints in materials property prediction tasks [\[Read\]](https://doi.org/10.1186/s13321-024-00811-6)
   Gupta, V., Li, Y., Peltekian, A. et al, *J Cheminform* **16**, 17 (2024)

   Abstract -
   Modern data mining techniques using machine learning (ML) and deep learning (DL) algorithms have been shown to excel in the regression-based task of materials property prediction using various materials representations. 
   <details>
   <summary>See More...</summary>
    In an attempt to improve the predictive performance of the deep neural network model, researchers have tried to add more layers as well as develop new architectural components to create sophisticated and deep neural network models that can aid in the training process and improve the predictive ability of the final model. However, usually, these modifications require a lot of computational resources, thereby further increasing the already large model training time, which is often not feasible, thereby limiting usage for most researchers. In this paper, we study and propose a deep neural network framework for regression-based problems comprising of fully connected layers that can work with any numerical vector-based materials representations as model input. We present a novel deep regression neural network, iBRNet, with branched skip connections and multiple schedulers, which can reduce the number of parameters used to construct the model, improve the accuracy, and decrease the training time of the predictive model. We perform the model training using composition-based numerical vectors representing the elemental fractions of the respective materials and compare their performance against other traditional ML and several known DL architectures. Using multiple datasets with varying data sizes for training and testing, We show that the proposed iBRNet models outperform the state-of-the-art ML and DL models for all data sizes. We also show that the branched structure and usage of multiple schedulers lead to fewer parameters and faster model training time with better convergence than other neural networks. Scientific contribution: The combination of multiple callback functions in deep neural networks minimizes training time and maximizes accuracy in a controlled computational environment with parametric constraints for the task of materials property prediction.
   </details>

---

2. ### Ionic species representations for materials informatics  [\[Read\]](https://chemrxiv.org/engage/chemrxiv/article-details/66acbd865101a2ffa8eaa181)
   Anthony Onwuli, Keith T. Butler, Aron Walsh, ChemRxiv. 2024; doi:10.26434/chemrxiv-2024-8621

   Abstract - 
    High-dimensional representations of the elements have become common within the field of materials informatics to build useful, structure-agnostic models for the chemistry of materials.
   <details>
       <summary>See More...</summary>
   However, the characteristics of elements change when they adopt a given oxidation state, with distinct structural preferences and physical properties. We explore several methods for developing embedding vectors of elements decorated with oxidation states. Graphs generated from 110,160 crystals are used to train representations of 84 elements that form 336 species. Clustering these learned representations of ionic species in low-dimensional space reproduces expected chemical heuristics, in particular the separation of cations from anions. We show that these representations have enhanced expressive power for property prediction tasks involving inorganic compounds. We expect that ionic representations, necessary for the description of mixed valence and complex magnetic systems, will support more powerful machine learning models for materials.
   </details>

---

3. ### Kernel fusion in atomistic spin dynamics simulations on Nvidia GPUs using tensor compare [\[Read\]](https://doi.org/10.1016/j.jocs.2024.102357)
   Hongwei Chen, Shiyang Chen, Joshua J. Turner, and Adrian Feiguin 
 
   Abstract - 
   In atomistic spin dynamics simulations, the time cost of constructing the space- and time-displaced pair correlation function in real space increases quadratically as the number of spins, leading to significant computational effort.
   <details>
       <summary>See More...</summary>
    The GEMM subroutine can be adopted to accelerate the calculation of the dynamical spin–spin correlation function, but the computational cost of simulating large spin systems (spins) on CPUs remains expensive. In this work, we perform the simulation on a graphics processing unit (GPU), a hardware solution widely used as an accelerator for scientific computing and deep learning. We show that GPUs can accelerate the simulation up to 25-fold compared to multi-core CPUs when using the GEMM subroutine on both. To hide memory latency, we fuse the element-wise operation into the GEMM kernel using which can improve the performance by 26% ~ 33% compared to the implementation based on. Furthermore, we perform the ‘on-the-fly’ calculation in the epilogue of the GEMM subroutine to avoid saving intermediate results on global memory, which makes large-scale atomistic spin dynamics simulations feasible and affordable.
    </details>

---

4. ### No more soggy cookies: The optimal cookie dunking time [\[Read\]](https://usustatesman.com/no-more-soggy-cookies-the-optimal-cookie-dunking-time/)
   Randy Hurd, Ben Roden and Tadd Truscott, The Utah Statesman

   Abstract - 
   We have all taken that terrifying risk with our chubby, cookie-laden fingers wedged into a glass of ice-cold milk, asking if we can wait just a little longer. We imagine that perfectly soaked, soft and flavorful cookie, while simultaneously overcome with the fear of what may result if we wait too long. To prevent this dunking-based anxiety, I have dedicated a lonely weekend to finding the optimal cooking dunking time.

---


5. ### Recent and Upcoming Developments in Randomized Numerical Linear Algebra for Machine Learning [\[Read\]](https://arxiv.org/abs/2406.11151)
   Michał Dereziński, Michael W. Mahoney, arXiv:2406.11151 (2024)

   Abstract - 
   Large matrices arise in many machine learning and data analysis applications, including as representations of datasets, graphs, model weights, and first and second-order derivatives. 
   <details>
       <summary>See More...</summary>
   Randomized Numerical Linear Algebra (RandNLA) is an area which uses randomness to develop improved algorithms for ubiquitous matrix problems. The area has reached a certain level of maturity; but recent hardware trends, efforts to incorporate RandNLA algorithms into core numerical libraries, and advances in machine learning, statistics, and random matrix theory, have lead to new theoretical and practical challenges. This article provides a self-contained overview of RandNLA, in light of these developments. 
   </details>

---

6. ### A deep-learning algorithm to disentangle self-interacting dark matter and AGN feedback models [\[Read\]](https://doi.org/10.1038/s41550-024-02322-8)
   David Harvey, *Nat Astron* (2024)

   Abstract - 
   The nature of dark matter remains one of the greatest unanswered questions in science. The largest concentrations of dark matter appear to lie in galaxy clusters.
   <details>
       <summary>See More...</summary>
      By modifying the properties of dark matter, the distribution of mass in clusters is altered in an observable way. However, uncertain astrophysical mechanisms also alter the mass distribution, often mimicking the effect of different dark matter properties. Here I present a machine learning method that ‘learns’, from simulations, how the impact of dark matter self-interactions differs from that of astrophysical feedback. In the idealized case, my algorithm is 80% accurate at identifying whether a galaxy cluster harbours collisionless dark matter, dark matter with a self interaction cross-section, σDM/m = 0.1 cm2 g−1 or dark matter with σDM/m = 1 cm2 g−1. It is found that weak-lensing information primarily differentiates self-interacting dark matter, whereas X-ray information disentangles different models of astrophysical feedback. The data are forward modelled to imitate observations from Euclid and Chandra, and it is found that the model has a statistical error of σDM/m < 0.01 cm2 g−1 and is insensitive to shape-measurement bias and photometric-redshift errors. This method represents a way to analyse data from upcoming telescopes that are an order of magnitude more precise and many orders faster than current methods, enabling us to explore the properties of dark matter like never before.
    </details>

---

7. ### Possibility of reaching the predicted center of the “island of stability” via the radioactive beam‑induced fusion [\[Read\]](https://doi.org/10.1007/s41365-024-01542-x)
   Zhang, MH., Zou, Y., Wang, MC. et al., *NUCL SCI TECH* **35**, 161 (2024) 

   Abstract - 
   Based on the dinuclear system model, the synthesis of the predicted double-magic nuclei and was investigated via neutron-rich radioactive beam-induced fusion reactions.
   <details>
       <summary>See More...</summary>
      The reaction is predicted to be favorable for producing with a maximal ER cross section of . Investigations of the entrance channel effect reveal that the target is more promising for synthesizing than the neutron-rich targets and , because of the influence of the Coulomb barrier. For the synthesis of , the maximal ER cross section of emerges in the reaction , indicating the need for further advancements in both experimental facilities and reaction mechanisms.
   </details>

---

8. ### Evaluation of thermodynamic equations of state across chemistry and structure in the materials project [\[Read\]](https://doi.org/10.1038/s41524-018-0091-x)
    Katherine Latimer, Shyam Dwaraknath, Kiran Mathew, Donald Winston & Kristin A. Persson, *npj Comput Mater* **4**, 40 (2018)

    Abstract -
    Thermodynamic equations of state (EOS) for crystalline solids describe material behaviors under changes in pressure, volume, entropy and temperature, making them fundamental to scientific research in a wide range of fields including geophysics, energy storage and development of novel materials.    
    <details>
    <summary>See More...</summary>
    Despite over a century of theoretical development and experimental testing of energy–volume (E–V) EOS for solids, there is still a lack of consensus with regard to which equation is indeed optimal, as well as to what metric is most appropriate for making this judgment. In this study, several metrics were used to evaluate quality of fit for 8 different EOS across 87 elements and over 100 compounds which appear in the literature. Our findings do not indicate a clear “best” EOS, but we identify three which consistently perform well relative to the rest of the set. Furthermore, we find that for the aggregate data set, the RMSrD is not strongly correlated with the nature of the compound, e.g., whether it is a metal, insulator, or semiconductor, nor the bulk modulus for any of the EOS, indicating that a single equation can be used across a broad range of classes of materials.
    </details>

