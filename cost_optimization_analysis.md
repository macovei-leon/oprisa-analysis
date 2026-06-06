# RAPORT DE ANALIZĂ A STRUCTURII DE COSTURI ȘI PLAN DE EFICIENTIZARE A FLOTEI

**Autor**: Antigravity AI Coding Assistant  
**Data**: 6 Iunie 2026  
**Workspace**: [analiza-3](file:///c:/Users/user/Desktop/analiza-3)  
**Sursa Datelor**: [new data](file:///c:/Users/user/Desktop/analiza-3/new%20data) și [Reports Statistics Trip Activity and Salaries](file:///c:/Users/user/Desktop/analiza-3/new%20data/Reports%20Statistics%20Trip%20Activity%20and%20Salaries)  

---

## 1. Introducere și Obiective Strategice

Acest raport prezintă o analiză aprofundată a structurii de costuri pe angajat/oră pentru toate cele 17 orașe active în care operăm ca partener de flotă Uber. Scopul principal este stabilirea unui plan concret de restructurare a flotei pentru a aduce costul mediu per angajat/oră (**`Tax+margin cost AVG`**) sub pragul critic de **22.50 EUR/oră**.

În prezent, operăm în pierdere structurală în majoritatea orașelor deoarece:
1. **Marja fixă de 8%** primită de la Uber nu acoperă costurile ridicate cu salariile fixe (13.90 EUR/h), taxele angajatorului și decontarea kilometrilor (0.20 EUR/km pentru biciclete, 0.30 EUR/km pentru mașini).
2. **Productivitatea scăzută (Trips per Hour - TPH)**: Mulți șoferi lucrează ture lungi (11-12 ore) având o medie de doar ~1-2 comenzi pe oră, ceea ce ne forțează să plătim salarii orare mari și compensații de kilometri fără ca aceștia să genereze venituri suficiente.
3. **Creșterea de sezon (Vârful de Vară)**: În următoarele 5-10 săptămâni, volumul de comenzi va crește semnificativ (conform datelor de forecast, care arată o creștere de peste 60% în Berlin și München, și de peste 138% în Leipzig). Totuși, mulți șoferi vor intra în concediu. Trebuie să angajăm exact profilul de contract și vehicul optim pentru a maximiza profitul din comenzi suplimentare.

---

## 2. Metodologia de Calcul și Analiza Matematică

Formula de calcul pentru costul total orar cu taxe și marja inclusă (**`Tax+margin cost AVG`**) este:

$$\text{Cost per Oră} = (\text{Salariu de bază} + \text{KPH} \times \text{Tarif Km}) \times (1 + \text{Procent Taxă}) \times 1.08$$

Unde:
- **Salariu de bază** = $13.90 \text{ EUR/oră}$
- **Tarif Km** = $0.20 \text{ EUR/km pentru Bicicletă}$, $0.30 \text{ EUR/km pentru Mașină}$
- **KPH** = Kilometri parcurși pe oră (Km/hour AVG)
- **Procent Taxă** = Taxe sociale și provizioane ale angajatorului: Minijob = $52.39\%$, Teilzeit (TZ) = $43.09\%$, Werkstudent = $31.89\%$, Sezonier (Kurzfristige Beschäftigung) = $3.00\% \text{ - } 15.00\%$
- **1.08** = Multiplicatorul de marjă orară al flotei (8%)

Pentru a respecta limita de **22.50 EUR/oră**, costul brut (inclusiv taxe, dar fără marja de 8%) trebuie să fie de maximum:

$$\text{Cost brut per oră} \le \frac{22.50}{1.08} = 20.8333 \text{ EUR/oră}$$

Prin urmare, relația devine:

$$13.90 + \text{KPH} \times \text{Tarif Km} \le \frac{20.8333}{1 + \text{Procent Taxă}}$$

### Analiza structurală pe tipuri de contracte:

> [!WARNING]
> **1. Minijob (Taxă = 52.39%)**
> Costul de bază orar la 0 km/h este:  
> $$13.90 \times 1.5239 \times 1.08 = \mathbf{22.88 \text{ EUR/oră}}$$
> Acest cost depășește deja limita de 22.50 EUR, chiar și fără a lua în calcul kilometrii parcurși! Prin urmare, **contractele de tip Minijob sunt matematic neviabile** și trebuie eliminate complet din flotă.

> [!WARNING]
> **2. Teilzeit / TZ (Taxă = 43.09%)**
> Costul de bază orar la 0 km/h este:  
> $$13.90 \times 1.4309 \times 1.08 = 21.48 \text{ EUR/oră}$$
> Spațiul rămas pentru decontarea kilometrilor este de doar $22.50 - 21.48 = 1.02 \text{ EUR/oră}$ (brut $0.66 \text{ EUR/oră}$).
> - Pentru **Bicicletă**: $\text{KPH maxim} = 0.66 / 0.20 = \mathbf{3.30 \text{ km/h}}$
> - Pentru **Mașină**: $\text{KPH maxim} = 0.66 / 0.30 = \mathbf{2.20 \text{ km/h}}$
> Deoarece curierii noștri parcurg în medie 8-15 km/h, **contractul Teilzeit este neviabil** și va genera mereu un cost peste 22.50 EUR/oră.

> [!NOTE]
> **3. Werkstudent (Taxă = 31.89%)**
> Costul de bază orar la 0 km/h este:  
> $$13.90 \times 1.3189 \times 1.08 = 19.80 \text{ EUR/oră}$$
> Spațiul rămas pentru kilometri este de $22.50 - 19.80 = 2.70 \text{ EUR/oră}$ (brut $1.896 \text{ EUR/oră}$).
> - Pentru **Bicicletă**: $\text{KPH maxim} = 1.896 / 0.20 = \mathbf{9.48 \text{ km/h}}$
> - Pentru **Mașină**: $\text{KPH maxim} = 1.896 / 0.30 = \mathbf{6.32 \text{ km/h}}$
> Deoarece curierii pe bicicletă au o viteză medie de 5-8 km/h (incluzând timpii de așteptare la restaurante), **Werkstudent + Bicicletă este singurul contract standard pe deplin viabil** (medie reală de ~21.50 EUR/oră). În schimb, Werkstudent + Mașină depășește limita din cauza vitezei medii de peste 10-15 km/h.

> [!TIP]
> **4. Student Sezonier / Kurzfristige Beschäftigung (Taxă = 3% - 15%)**
> Exonerarea de la plata contribuțiilor de asigurări sociale pe o perioadă de maximum 3 luni reduce taxele angajatorului la doar ~3% (taxe U1/U2/accident + fără provizioane) sau 15% (dacă includem provizioanele).
> La o taxă optimistă de **3.0%**:
> - Costul de bază orar la 0 km/h: $$13.90 \times 1.03 \times 1.08 = 15.46 \text{ EUR/oră}$$
> - Pentru **Bicicletă**: $\text{KPH maxim} = \mathbf{31.63 \text{ km/h}}$ (întotdeauna conform)
> - Pentru **Mașină**: $\text{KPH maxim} = \mathbf{21.09 \text{ km/h}}$ (conform pentru majoritatea mașinilor, care au medii de 10-15 km/h!)
> Acest contract este **extrem de rațional** și trebuie utilizat pe scară largă pentru vârful de vară în Berlin și alte centre universitare.

> [!IMPORTANT]
> **5. Politica Internă de Căpuire a Kilometrilor (Abordare de Tip Gewerbe pe Contracte)**
> - Toți curierii noștri lucrează **exclusiv pe contracte de muncă standard** (Minijob, Teilzeit, Werkstudent, Sezonier), nu ca freelanceri (Gewerbe).
> - Totuși, pentru a proteja profitabilitatea în cazul șoferilor care lucrează multe ore cu productivitate scăzută (ceea ce ne duce pe minus), aplicăm o politică internă de tip *Gewerbe*: plătim decontarea kilometrilor în mod normal, dar **sistemul oprește plata kilometrilor în momentul în care firma intră în minus** pe acel șofer (marja din comisionul curselor sale nu acoperă costul salarial orar brut).

---

## 3. Clasificarea Flotei în Ordine Descrescătoare a Raționalității Costurilor

Pentru a reduce costurile și a asigura respectarea pragului de 22.50 EUR/oră, iată ierarhia opțiunilor de angajare (de la cea mai rațională la cea mai puțin rațională):

| Poz | Tip Contract | Vehicul | Procent Taxă | Cost Mediu Estimare (EUR/h) | TPH Real Mediu | Status Conformitate (Cap 22.50) | Decizie Operațională |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | Sezonier (Kurzfristig) | Bicicletă | 3.00% | 16.50 - 17.50 | 2.00 | **Conform (Optim)** | **Angajare masivă studenți vara** |
| **2** | Sezonier (Kurzfristig) | Mașină | 3.00% | 19.00 - 20.50 | 2.00 | **Conform (Optim)** | **Utilizare temporară pe vară** |
| **3** | Werkstudent | Bicicletă | 31.89% | 21.00 - 22.00 | 2.03 | **Conform (Sub limită)** | **Angajare permanentă de bază** |
| **4** | Werkstudent | Mașină | 31.89% | 23.00 - 25.00 | 2.03 | *Neconform (Depășește)* | **Tranziție la Bicicletă / Căpuire Km** |
| **5** | Teilzeit / TZ | Bicicletă | 43.09% | 23.50 - 24.50 | 1.99 | *Neconform (Depășește)* | **Fără angajări noi / Tranzit** |
| **6** | Teilzeit / TZ | Mașină | 43.09% | 26.50 - 28.00 | 2.00 | *Neconform (Depășește)* | **Restructurare / Concediere** |
| **7** | Minijob | Bicicletă | 52.39% | 24.50 - 25.50 | 2.00 | *Neconform (Depășește)* | **Eliminare completă din flotă** |
| **8** | Minijob | Mașină | 52.39% | 27.50 - 29.50 | 2.00 | *Neconform (Depășește)* | **Eliminare completă din flotă** |


---

## 4. Analiza specifică pe orașe și Planuri de acțiune

Prezentăm mai jos situația actuală din fiecare oraș (ordonată descrescător după costul orar actual) și pașii clari pentru a ajunge la costul orar maxim de 22.50 EUR.

### Bonn
- **Ore active în Mai**: 75.00 h
- **Cost mediu orar actual**: **29.09 EUR/h** (Depășește pragul cu **6.59 EUR/h**)
- **TPH mediu actual**: 1.89 livrări/h | **KPH mediu actual**: 12.67 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 73.0 h (97.3%) | Cost: 29.24 EUR/h | TPH: 1.92 | KPH: 12.89
  - `TZ` + `Car`: 2.0 h (2.7%) | Cost: 23.63 EUR/h | TPH: 1.00 | KPH: 4.63
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Kassel
- **Ore active în Mai**: 101.00 h
- **Cost mediu orar actual**: **28.69 EUR/h** (Depășește pragul cu **6.19 EUR/h**)
- **TPH mediu actual**: 2.24 livrări/h | **KPH mediu actual**: 11.77 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 101.0 h (100.0%) | Cost: 28.69 EUR/h | TPH: 2.24 | KPH: 11.77
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Paderborn
- **Ore active în Mai**: 1,324.00 h
- **Cost mediu orar actual**: **28.69 EUR/h** (Depășește pragul cu **6.19 EUR/h**)
- **TPH mediu actual**: 2.12 livrări/h | **KPH mediu actual**: 13.45 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 711.0 h (53.7%) | Cost: 29.61 EUR/h | TPH: 2.11 | KPH: 13.64
  - `TZ` + `Car`: 613.0 h (46.3%) | Cost: 27.61 EUR/h | TPH: 2.13 | KPH: 13.22
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Siegen
- **Ore active în Mai**: 30.00 h
- **Cost mediu orar actual**: **28.64 EUR/h** (Depășește pragul cu **6.14 EUR/h**)
- **TPH mediu actual**: 2.17 livrări/h | **KPH mediu actual**: 11.68 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 30.0 h (100.0%) | Cost: 28.64 EUR/h | TPH: 2.17 | KPH: 11.68
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Saarbruecken
- **Ore active în Mai**: 103.00 h
- **Cost mediu orar actual**: **28.50 EUR/h** (Depășește pragul cu **6.00 EUR/h**)
- **TPH mediu actual**: 2.04 livrări/h | **KPH mediu actual**: 11.39 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 103.0 h (100.0%) | Cost: 28.50 EUR/h | TPH: 2.04 | KPH: 11.39
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Troisdorf
- **Ore active în Mai**: 32.00 h
- **Cost mediu orar actual**: **28.41 EUR/h** (Depășește pragul cu **5.91 EUR/h**)
- **TPH mediu actual**: 1.72 livrări/h | **KPH mediu actual**: 12.12 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 24.0 h (75.0%) | Cost: 28.75 EUR/h | TPH: 1.71 | KPH: 11.89
  - `TZ` + `Car`: 8.0 h (25.0%) | Cost: 27.41 EUR/h | TPH: 1.75 | KPH: 12.80
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Munich
- **Ore active în Mai**: 28,586.00 h
- **Cost mediu orar actual**: **28.29 EUR/h** (Depășește pragul cu **5.79 EUR/h**)
- **TPH mediu actual**: 2.12 livrări/h | **KPH mediu actual**: 15.03 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 433.0 h (1.5%) | Cost: 25.46 EUR/h | TPH: 2.27 | KPH: 7.85
  - `Minijob` + `Car`: 1757.0 h (6.1%) | Cost: 30.03 EUR/h | TPH: 2.14 | KPH: 14.48
  - `TZ` + `Bicycle`: 3124.0 h (10.9%) | Cost: 25.72 EUR/h | TPH: 2.06 | KPH: 13.70
  - `TZ` + `Car`: 22886.0 h (80.1%) | Cost: 28.67 EUR/h | TPH: 2.12 | KPH: 15.50
  - `Werkstundent` + `Bicycle`: 358.0 h (1.3%) | Cost: 22.19 EUR/h | TPH: 2.08 | KPH: 8.40
  - `Werkstundent` + `Car`: 28.0 h (0.1%) | Cost: 25.45 EUR/h | TPH: 1.75 | KPH: 13.23
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Tranziție către Biciclete (Congestie urbană)**: Deoarece Munich are o congestie ridicată (Frankfurt/München au blocaje masive în centru), viteza mașinilor este redusă iar timpul de parcare este mare. BTPH (TPH pe bicicletă) este istoric mai mare sau egal cu cel auto în centru. Se recomandă înlocuirea mașinilor cu biciclete electrice în proporție de **80% biciclete / 20% mașini** pentru livrările ultra-centrale.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Cologne
- **Ore active în Mai**: 1,450.00 h
- **Cost mediu orar actual**: **28.11 EUR/h** (Depășește pragul cu **5.61 EUR/h**)
- **TPH mediu actual**: 2.08 livrări/h | **KPH mediu actual**: 14.02 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 106.0 h (7.3%) | Cost: 29.98 EUR/h | TPH: 2.27 | KPH: 14.39
  - `TZ` + `Bicycle`: 3.0 h (0.2%) | Cost: 24.51 EUR/h | TPH: 1.67 | KPH: 9.80
  - `TZ` + `Car`: 1341.0 h (92.5%) | Cost: 27.97 EUR/h | TPH: 2.06 | KPH: 14.00
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Tranziție către Biciclete (Congestie urbană)**: Deoarece Cologne are o congestie ridicată (Cologne are 67h pierdute pe an, fiind cea mai blocată), viteza mașinilor este redusă iar timpul de parcare este mare. BTPH (TPH pe bicicletă) este istoric mai mare sau egal cu cel auto în centru. Se recomandă înlocuirea mașinilor cu biciclete electrice în proporție de **80% biciclete / 20% mașini** pentru livrările ultra-centrale.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Frankfurt am Main
- **Ore active în Mai**: 24,084.00 h
- **Cost mediu orar actual**: **28.11 EUR/h** (Depășește pragul cu **5.61 EUR/h**)
- **TPH mediu actual**: 1.94 livrări/h | **KPH mediu actual**: 14.61 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 169.0 h (0.7%) | Cost: 26.91 EUR/h | TPH: 2.07 | KPH: 12.24
  - `Minijob` + `Car`: 1271.0 h (5.3%) | Cost: 29.48 EUR/h | TPH: 1.85 | KPH: 13.37
  - `TZ` + `Bicycle`: 2663.0 h (11.1%) | Cost: 25.79 EUR/h | TPH: 2.01 | KPH: 13.95
  - `TZ` + `Car`: 19981.0 h (83.0%) | Cost: 28.34 EUR/h | TPH: 1.94 | KPH: 14.80
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Tranziție către Biciclete (Congestie urbană)**: Deoarece Frankfurt am Main are o congestie ridicată (Frankfurt/München au blocaje masive în centru), viteza mașinilor este redusă iar timpul de parcare este mare. BTPH (TPH pe bicicletă) este istoric mai mare sau egal cu cel auto în centru. Se recomandă înlocuirea mașinilor cu biciclete electrice în proporție de **80% biciclete / 20% mașini** pentru livrările ultra-centrale.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Trier
- **Ore active în Mai**: 941.00 h
- **Cost mediu orar actual**: **28.08 EUR/h** (Depășește pragul cu **5.58 EUR/h**)
- **TPH mediu actual**: 2.37 livrări/h | **KPH mediu actual**: 13.30 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 24.0 h (2.6%) | Cost: 25.14 EUR/h | TPH: 2.17 | KPH: 6.86
  - `Minijob` + `Car`: 221.0 h (23.5%) | Cost: 29.75 EUR/h | TPH: 2.49 | KPH: 13.93
  - `TZ` + `Car`: 696.0 h (74.0%) | Cost: 27.66 EUR/h | TPH: 2.33 | KPH: 13.32
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Aachen
- **Ore active în Mai**: 40.00 h
- **Cost mediu orar actual**: **28.03 EUR/h** (Depășește pragul cu **5.53 EUR/h**)
- **TPH mediu actual**: 1.77 livrări/h | **KPH mediu actual**: 11.38 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 32.0 h (80.0%) | Cost: 28.62 EUR/h | TPH: 1.78 | KPH: 11.64
  - `TZ` + `Bicycle`: 2.0 h (5.0%) | Cost: 26.29 EUR/h | TPH: 2.50 | KPH: 15.54
  - `TZ` + `Car`: 6.0 h (15.0%) | Cost: 25.48 EUR/h | TPH: 1.50 | KPH: 8.62
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Stuttgart
- **Ore active în Mai**: 796.00 h
- **Cost mediu orar actual**: **27.90 EUR/h** (Depășește pragul cu **5.40 EUR/h**)
- **TPH mediu actual**: 1.91 livrări/h | **KPH mediu actual**: 13.17 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 144.0 h (18.1%) | Cost: 28.67 EUR/h | TPH: 1.71 | KPH: 11.73
  - `TZ` + `Bicycle`: 2.0 h (0.3%) | Cost: 23.17 EUR/h | TPH: 1.00 | KPH: 5.48
  - `TZ` + `Car`: 650.0 h (81.7%) | Cost: 27.74 EUR/h | TPH: 1.96 | KPH: 13.51
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Tranziție către Biciclete (Congestie urbană)**: Deoarece Stuttgart are o congestie ridicată (Frankfurt/München au blocaje masive în centru), viteza mașinilor este redusă iar timpul de parcare este mare. BTPH (TPH pe bicicletă) este istoric mai mare sau egal cu cel auto în centru. Se recomandă înlocuirea mașinilor cu biciclete electrice în proporție de **80% biciclete / 20% mașini** pentru livrările ultra-centrale.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Bochum
- **Ore active în Mai**: 224.00 h
- **Cost mediu orar actual**: **27.87 EUR/h** (Depășește pragul cu **5.37 EUR/h**)
- **TPH mediu actual**: 1.80 livrări/h | **KPH mediu actual**: 11.53 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 134.0 h (59.8%) | Cost: 28.49 EUR/h | TPH: 1.96 | KPH: 11.37
  - `TZ` + `Car`: 90.0 h (40.2%) | Cost: 26.94 EUR/h | TPH: 1.58 | KPH: 11.77
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Luebeck
- **Ore active în Mai**: 491.00 h
- **Cost mediu orar actual**: **27.86 EUR/h** (Depășește pragul cu **5.36 EUR/h**)
- **TPH mediu actual**: 2.10 livrări/h | **KPH mediu actual**: 13.77 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `TZ` + `Bicycle`: 1.0 h (0.2%) | Cost: 23.04 EUR/h | TPH: 1.00 | KPH: 5.05
  - `TZ` + `Car`: 490.0 h (99.8%) | Cost: 27.87 EUR/h | TPH: 2.10 | KPH: 13.78
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Menținerea interdicției pe Minijobs**: Nu se vor aproba contracte noi de tip Minijob în acest oraș.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Karlsruhe
- **Ore active în Mai**: 2,928.00 h
- **Cost mediu orar actual**: **27.82 EUR/h** (Depășește pragul cu **5.32 EUR/h**)
- **TPH mediu actual**: 2.36 livrări/h | **KPH mediu actual**: 13.06 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 69.0 h (2.4%) | Cost: 25.46 EUR/h | TPH: 2.45 | KPH: 7.84
  - `Minijob` + `Car`: 526.0 h (18.0%) | Cost: 28.14 EUR/h | TPH: 2.25 | KPH: 10.67
  - `TZ` + `Bicycle`: 75.0 h (2.6%) | Cost: 24.08 EUR/h | TPH: 2.56 | KPH: 8.42
  - `TZ` + `Car`: 2258.0 h (77.1%) | Cost: 27.94 EUR/h | TPH: 2.37 | KPH: 13.93
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Heidelberg
- **Ore active în Mai**: 4,112.00 h
- **Cost mediu orar actual**: **27.82 EUR/h** (Depășește pragul cu **5.32 EUR/h**)
- **TPH mediu actual**: 2.39 livrări/h | **KPH mediu actual**: 13.46 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 1.0 h (0.0%) | Cost: 25.80 EUR/h | TPH: 1.00 | KPH: 8.88
  - `Minijob` + `Car`: 216.0 h (5.3%) | Cost: 29.69 EUR/h | TPH: 2.52 | KPH: 13.81
  - `TZ` + `Car`: 3895.0 h (94.7%) | Cost: 27.71 EUR/h | TPH: 2.38 | KPH: 13.44
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Dusseldorf
- **Ore active în Mai**: 4,353.00 h
- **Cost mediu orar actual**: **27.41 EUR/h** (Depășește pragul cu **4.91 EUR/h**)
- **TPH mediu actual**: 2.34 livrări/h | **KPH mediu actual**: 13.19 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 25.0 h (0.6%) | Cost: 24.65 EUR/h | TPH: 1.96 | KPH: 5.39
  - `Minijob` + `Car`: 314.0 h (7.2%) | Cost: 29.29 EUR/h | TPH: 2.46 | KPH: 12.99
  - `TZ` + `Bicycle`: 657.0 h (15.1%) | Cost: 25.66 EUR/h | TPH: 2.19 | KPH: 13.52
  - `TZ` + `Car`: 3357.0 h (77.1%) | Cost: 27.60 EUR/h | TPH: 2.36 | KPH: 13.20
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Tranziție către Biciclete (Congestie urbană)**: Deoarece Dusseldorf are o congestie ridicată (Frankfurt/München au blocaje masive în centru), viteza mașinilor este redusă iar timpul de parcare este mare. BTPH (TPH pe bicicletă) este istoric mai mare sau egal cu cel auto în centru. Se recomandă înlocuirea mașinilor cu biciclete electrice în proporție de **80% biciclete / 20% mașini** pentru livrările ultra-centrale.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Freiburg im Breisgau
- **Ore active în Mai**: 2,447.00 h
- **Cost mediu orar actual**: **27.20 EUR/h** (Depășește pragul cu **4.70 EUR/h**)
- **TPH mediu actual**: 2.11 livrări/h | **KPH mediu actual**: 11.74 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 546.0 h (22.3%) | Cost: 27.90 EUR/h | TPH: 2.20 | KPH: 10.18
  - `TZ` + `Bicycle`: 218.0 h (8.9%) | Cost: 23.77 EUR/h | TPH: 1.99 | KPH: 7.41
  - `TZ` + `Car`: 1683.0 h (68.8%) | Cost: 27.42 EUR/h | TPH: 2.09 | KPH: 12.81
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Wiesbaden
- **Ore active în Mai**: 2,047.00 h
- **Cost mediu orar actual**: **27.08 EUR/h** (Depășește pragul cu **4.58 EUR/h**)
- **TPH mediu actual**: 2.02 livrări/h | **KPH mediu actual**: 11.17 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 53.0 h (2.6%) | Cost: 26.77 EUR/h | TPH: 2.15 | KPH: 11.82
  - `Minijob` + `Car`: 705.0 h (34.4%) | Cost: 28.54 EUR/h | TPH: 2.23 | KPH: 11.46
  - `TZ` + `Bicycle`: 224.0 h (10.9%) | Cost: 24.68 EUR/h | TPH: 1.54 | KPH: 10.35
  - `TZ` + `Car`: 1065.0 h (52.0%) | Cost: 26.63 EUR/h | TPH: 1.98 | KPH: 11.11
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Heilbronn
- **Ore active în Mai**: 2,186.00 h
- **Cost mediu orar actual**: **27.08 EUR/h** (Depășește pragul cu **4.58 EUR/h**)
- **TPH mediu actual**: 2.17 livrări/h | **KPH mediu actual**: 12.49 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 393.0 h (18.0%) | Cost: 29.07 EUR/h | TPH: 2.38 | KPH: 12.54
  - `TZ` + `Bicycle`: 584.0 h (26.7%) | Cost: 25.30 EUR/h | TPH: 2.11 | KPH: 12.37
  - `TZ` + `Car`: 1209.0 h (55.3%) | Cost: 27.29 EUR/h | TPH: 2.13 | KPH: 12.52
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Wuerzburg
- **Ore active în Mai**: 319.00 h
- **Cost mediu orar actual**: **27.04 EUR/h** (Depășește pragul cu **4.54 EUR/h**)
- **TPH mediu actual**: 2.00 livrări/h | **KPH mediu actual**: 12.14 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `TZ` + `Car`: 311.0 h (97.5%) | Cost: 27.17 EUR/h | TPH: 1.98 | KPH: 12.27
  - `Werkstundent` + `Bicycle`: 8.0 h (2.5%) | Cost: 21.81 EUR/h | TPH: 2.50 | KPH: 7.04
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Menținerea interdicției pe Minijobs**: Nu se vor aproba contracte noi de tip Minijob în acest oraș.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Regensburg
- **Ore active în Mai**: 619.00 h
- **Cost mediu orar actual**: **26.96 EUR/h** (Depășește pragul cu **4.46 EUR/h**)
- **TPH mediu actual**: 2.07 livrări/h | **KPH mediu actual**: 10.75 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 173.0 h (27.9%) | Cost: 28.79 EUR/h | TPH: 2.29 | KPH: 11.98
  - `TZ` + `Car`: 446.0 h (72.1%) | Cost: 26.25 EUR/h | TPH: 1.98 | KPH: 10.28
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Dortmund
- **Ore active în Mai**: 1,180.00 h
- **Cost mediu orar actual**: **26.91 EUR/h** (Depășește pragul cu **4.41 EUR/h**)
- **TPH mediu actual**: 2.05 livrări/h | **KPH mediu actual**: 11.61 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 28.0 h (2.4%) | Cost: 28.01 EUR/h | TPH: 1.50 | KPH: 10.39
  - `TZ` + `Car`: 1152.0 h (97.6%) | Cost: 26.88 EUR/h | TPH: 2.07 | KPH: 11.64
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Herne
- **Ore active în Mai**: 111.00 h
- **Cost mediu orar actual**: **26.87 EUR/h** (Depășește pragul cu **4.37 EUR/h**)
- **TPH mediu actual**: 1.20 livrări/h | **KPH mediu actual**: 9.40 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 72.0 h (64.9%) | Cost: 27.29 EUR/h | TPH: 1.15 | KPH: 8.94
  - `TZ` + `Bicycle`: 5.0 h (4.5%) | Cost: 23.41 EUR/h | TPH: 1.20 | KPH: 6.26
  - `TZ` + `Car`: 34.0 h (30.6%) | Cost: 26.50 EUR/h | TPH: 1.29 | KPH: 10.83
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Wuppertal
- **Ore active în Mai**: 115.00 h
- **Cost mediu orar actual**: **26.79 EUR/h** (Depășește pragul cu **4.29 EUR/h**)
- **TPH mediu actual**: 1.95 livrări/h | **KPH mediu actual**: 10.71 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 23.0 h (20.0%) | Cost: 28.14 EUR/h | TPH: 1.78 | KPH: 10.66
  - `TZ` + `Car`: 92.0 h (80.0%) | Cost: 26.45 EUR/h | TPH: 1.99 | KPH: 10.72
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Osnabrueck
- **Ore active în Mai**: 1,019.00 h
- **Cost mediu orar actual**: **26.78 EUR/h** (Depășește pragul cu **4.28 EUR/h**)
- **TPH mediu actual**: 2.00 livrări/h | **KPH mediu actual**: 10.27 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 322.0 h (31.6%) | Cost: 27.77 EUR/h | TPH: 2.14 | KPH: 9.91
  - `TZ` + `Car`: 697.0 h (68.4%) | Cost: 26.32 EUR/h | TPH: 1.94 | KPH: 10.43
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Ingolstadt
- **Ore active în Mai**: 2,315.00 h
- **Cost mediu orar actual**: **26.63 EUR/h** (Depășește pragul cu **4.13 EUR/h**)
- **TPH mediu actual**: 1.99 livrări/h | **KPH mediu actual**: 11.40 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 366.0 h (15.8%) | Cost: 28.70 EUR/h | TPH: 2.06 | KPH: 11.79
  - `TZ` + `Bicycle`: 403.0 h (17.4%) | Cost: 25.35 EUR/h | TPH: 2.16 | KPH: 12.51
  - `TZ` + `Car`: 1477.0 h (63.8%) | Cost: 26.72 EUR/h | TPH: 1.95 | KPH: 11.30
  - `Werkstundent` + `Bicycle`: 69.0 h (3.0%) | Cost: 21.23 EUR/h | TPH: 1.46 | KPH: 5.01
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Guetersloh
- **Ore active în Mai**: 128.00 h
- **Cost mediu orar actual**: **26.58 EUR/h** (Depășește pragul cu **4.08 EUR/h**)
- **TPH mediu actual**: 1.58 livrări/h | **KPH mediu actual**: 7.52 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 127.0 h (99.2%) | Cost: 26.58 EUR/h | TPH: 1.58 | KPH: 7.51
  - `TZ` + `Car`: 1.0 h (0.8%) | Cost: 25.69 EUR/h | TPH: 1.00 | KPH: 9.09
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Bielefeld
- **Ore active în Mai**: 5,347.00 h
- **Cost mediu orar actual**: **26.47 EUR/h** (Depășește pragul cu **3.97 EUR/h**)
- **TPH mediu actual**: 2.16 livrări/h | **KPH mediu actual**: 11.44 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 93.0 h (1.7%) | Cost: 25.05 EUR/h | TPH: 2.04 | KPH: 6.62
  - `Minijob` + `Car`: 193.0 h (3.6%) | Cost: 28.22 EUR/h | TPH: 2.04 | KPH: 10.81
  - `TZ` + `Bicycle`: 997.0 h (18.6%) | Cost: 24.43 EUR/h | TPH: 2.13 | KPH: 9.53
  - `TZ` + `Car`: 3805.0 h (71.2%) | Cost: 27.14 EUR/h | TPH: 2.18 | KPH: 12.21
  - `Werkstundent` + `Bicycle`: 88.0 h (1.6%) | Cost: 21.26 EUR/h | TPH: 1.89 | KPH: 5.14
  - `Werkstundent` + `Car`: 171.0 h (3.2%) | Cost: 24.88 EUR/h | TPH: 2.36 | KPH: 11.88
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Mannheim
- **Ore active în Mai**: 692.00 h
- **Cost mediu orar actual**: **26.39 EUR/h** (Depășește pragul cu **3.89 EUR/h**)
- **TPH mediu actual**: 2.24 livrări/h | **KPH mediu actual**: 10.14 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 21.0 h (3.0%) | Cost: 26.95 EUR/h | TPH: 1.95 | KPH: 12.38
  - `Minijob` + `Car`: 149.0 h (21.5%) | Cost: 29.17 EUR/h | TPH: 2.12 | KPH: 12.74
  - `TZ` + `Bicycle`: 81.0 h (11.7%) | Cost: 24.24 EUR/h | TPH: 3.32 | KPH: 8.94
  - `TZ` + `Car`: 440.0 h (63.6%) | Cost: 25.83 EUR/h | TPH: 2.10 | KPH: 9.39
  - `Werkstundent` + `Bicycle`: 1.0 h (0.1%) | Cost: 20.58 EUR/h | TPH: 1.00 | KPH: 2.74
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Hanau
- **Ore active în Mai**: 847.00 h
- **Cost mediu orar actual**: **26.37 EUR/h** (Depășește pragul cu **3.87 EUR/h**)
- **TPH mediu actual**: 1.48 livrări/h | **KPH mediu actual**: 7.95 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 105.0 h (12.4%) | Cost: 25.32 EUR/h | TPH: 1.37 | KPH: 7.43
  - `Minijob` + `Car`: 604.0 h (71.3%) | Cost: 26.80 EUR/h | TPH: 1.52 | KPH: 7.96
  - `TZ` + `Bicycle`: 9.0 h (1.1%) | Cost: 23.60 EUR/h | TPH: 1.44 | KPH: 6.87
  - `TZ` + `Car`: 129.0 h (15.2%) | Cost: 25.39 EUR/h | TPH: 1.42 | KPH: 8.43
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Ulm
- **Ore active în Mai**: 2,122.00 h
- **Cost mediu orar actual**: **26.34 EUR/h** (Depășește pragul cu **3.84 EUR/h**)
- **TPH mediu actual**: 1.94 livrări/h | **KPH mediu actual**: 10.20 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 101.0 h (4.8%) | Cost: 25.06 EUR/h | TPH: 2.10 | KPH: 6.63
  - `Minijob` + `Car`: 275.0 h (13.0%) | Cost: 27.45 EUR/h | TPH: 1.79 | KPH: 9.27
  - `TZ` + `Bicycle`: 147.0 h (6.9%) | Cost: 24.60 EUR/h | TPH: 1.32 | KPH: 10.10
  - `TZ` + `Car`: 1599.0 h (75.4%) | Cost: 26.39 EUR/h | TPH: 2.02 | KPH: 10.59
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Augsburg
- **Ore active în Mai**: 5,117.00 h
- **Cost mediu orar actual**: **26.33 EUR/h** (Depășește pragul cu **3.83 EUR/h**)
- **TPH mediu actual**: 1.79 livrări/h | **KPH mediu actual**: 10.38 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 116.0 h (2.3%) | Cost: 24.81 EUR/h | TPH: 1.98 | KPH: 5.87
  - `Minijob` + `Car`: 418.0 h (8.2%) | Cost: 27.92 EUR/h | TPH: 1.82 | KPH: 10.21
  - `TZ` + `Bicycle`: 162.0 h (3.2%) | Cost: 23.22 EUR/h | TPH: 1.25 | KPH: 5.64
  - `TZ` + `Car`: 4266.0 h (83.4%) | Cost: 26.50 EUR/h | TPH: 1.78 | KPH: 10.82
  - `Werkstundent` + `Bicycle`: 155.0 h (3.0%) | Cost: 21.80 EUR/h | TPH: 2.41 | KPH: 7.01
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Hamburg
- **Ore active în Mai**: 6,524.00 h
- **Cost mediu orar actual**: **26.26 EUR/h** (Depășește pragul cu **3.76 EUR/h**)
- **TPH mediu actual**: 1.87 livrări/h | **KPH mediu actual**: 10.33 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 12.0 h (0.2%) | Cost: 24.10 EUR/h | TPH: 1.50 | KPH: 3.72
  - `Minijob` + `Car`: 205.0 h (3.1%) | Cost: 27.58 EUR/h | TPH: 1.86 | KPH: 9.52
  - `TZ` + `Bicycle`: 519.0 h (8.0%) | Cost: 23.19 EUR/h | TPH: 1.63 | KPH: 5.52
  - `TZ` + `Car`: 5788.0 h (88.7%) | Cost: 26.49 EUR/h | TPH: 1.89 | KPH: 10.81
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Essen
- **Ore active în Mai**: 2,081.00 h
- **Cost mediu orar actual**: **26.24 EUR/h** (Depășește pragul cu **3.74 EUR/h**)
- **TPH mediu actual**: 2.04 livrări/h | **KPH mediu actual**: 10.17 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 60.0 h (2.9%) | Cost: 28.04 EUR/h | TPH: 2.23 | KPH: 10.45
  - `TZ` + `Bicycle`: 6.0 h (0.3%) | Cost: 24.45 EUR/h | TPH: 1.17 | KPH: 9.60
  - `TZ` + `Car`: 2015.0 h (96.8%) | Cost: 26.19 EUR/h | TPH: 2.04 | KPH: 10.16
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Ludwigsburg
- **Ore active în Mai**: 520.00 h
- **Cost mediu orar actual**: **26.14 EUR/h** (Depășește pragul cu **3.64 EUR/h**)
- **TPH mediu actual**: 1.64 livrări/h | **KPH mediu actual**: 10.04 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 1.0 h (0.2%) | Cost: 26.13 EUR/h | TPH: 1.00 | KPH: 6.58
  - `TZ` + `Car`: 519.0 h (99.8%) | Cost: 26.14 EUR/h | TPH: 1.64 | KPH: 10.04
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Sindelfingen
- **Ore active în Mai**: 380.00 h
- **Cost mediu orar actual**: **26.06 EUR/h** (Depășește pragul cu **3.56 EUR/h**)
- **TPH mediu actual**: 1.62 livrări/h | **KPH mediu actual**: 8.90 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 109.0 h (28.7%) | Cost: 27.35 EUR/h | TPH: 1.77 | KPH: 9.05
  - `TZ` + `Bicycle`: 10.0 h (2.6%) | Cost: 23.43 EUR/h | TPH: 1.20 | KPH: 6.29
  - `TZ` + `Car`: 261.0 h (68.7%) | Cost: 25.62 EUR/h | TPH: 1.57 | KPH: 8.93
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Pforzheim
- **Ore active în Mai**: 521.00 h
- **Cost mediu orar actual**: **26.05 EUR/h** (Depășește pragul cu **3.55 EUR/h**)
- **TPH mediu actual**: 1.78 livrări/h | **KPH mediu actual**: 9.86 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `TZ` + `Car`: 521.0 h (100.0%) | Cost: 26.05 EUR/h | TPH: 1.78 | KPH: 9.86
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Menținerea interdicției pe Minijobs**: Nu se vor aproba contracte noi de tip Minijob în acest oraș.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Hannover
- **Ore active în Mai**: 690.00 h
- **Cost mediu orar actual**: **25.95 EUR/h** (Depășește pragul cu **3.45 EUR/h**)
- **TPH mediu actual**: 1.63 livrări/h | **KPH mediu actual**: 9.90 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 111.0 h (16.1%) | Cost: 28.54 EUR/h | TPH: 1.90 | KPH: 11.47
  - `TZ` + `Bicycle`: 196.0 h (28.4%) | Cost: 24.33 EUR/h | TPH: 1.73 | KPH: 9.23
  - `TZ` + `Car`: 383.0 h (55.5%) | Cost: 26.02 EUR/h | TPH: 1.50 | KPH: 9.79
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Mainz
- **Ore active în Mai**: 1,623.00 h
- **Cost mediu orar actual**: **25.93 EUR/h** (Depășește pragul cu **3.43 EUR/h**)
- **TPH mediu actual**: 1.63 livrări/h | **KPH mediu actual**: 10.09 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 97.0 h (6.0%) | Cost: 26.38 EUR/h | TPH: 1.75 | KPH: 10.63
  - `Minijob` + `Car`: 177.0 h (10.9%) | Cost: 28.06 EUR/h | TPH: 1.71 | KPH: 10.51
  - `TZ` + `Bicycle`: 442.0 h (27.2%) | Cost: 24.55 EUR/h | TPH: 1.60 | KPH: 9.93
  - `TZ` + `Car`: 907.0 h (55.9%) | Cost: 26.13 EUR/h | TPH: 1.62 | KPH: 10.04
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Offenbach
- **Ore active în Mai**: 3,429.00 h
- **Cost mediu orar actual**: **25.91 EUR/h** (Depășește pragul cu **3.41 EUR/h**)
- **TPH mediu actual**: 1.62 livrări/h | **KPH mediu actual**: 9.44 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 11.0 h (0.3%) | Cost: 25.28 EUR/h | TPH: 1.55 | KPH: 7.31
  - `Minijob` + `Car`: 398.0 h (11.6%) | Cost: 27.88 EUR/h | TPH: 1.68 | KPH: 10.14
  - `TZ` + `Bicycle`: 446.0 h (13.0%) | Cost: 23.79 EUR/h | TPH: 1.84 | KPH: 7.48
  - `TZ` + `Car`: 2574.0 h (75.1%) | Cost: 25.97 EUR/h | TPH: 1.57 | KPH: 9.68
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Nuremberg
- **Ore active în Mai**: 4,102.00 h
- **Cost mediu orar actual**: **25.84 EUR/h** (Depășește pragul cu **3.34 EUR/h**)
- **TPH mediu actual**: 1.81 livrări/h | **KPH mediu actual**: 10.01 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 193.0 h (4.7%) | Cost: 24.53 EUR/h | TPH: 2.11 | KPH: 5.04
  - `Minijob` + `Car`: 705.0 h (17.2%) | Cost: 28.24 EUR/h | TPH: 1.72 | KPH: 10.86
  - `TZ` + `Bicycle`: 562.0 h (13.7%) | Cost: 24.45 EUR/h | TPH: 1.80 | KPH: 9.62
  - `TZ` + `Car`: 2041.0 h (49.8%) | Cost: 26.79 EUR/h | TPH: 1.75 | KPH: 11.44
  - `Werkstundent` + `Bicycle`: 593.0 h (14.5%) | Cost: 21.54 EUR/h | TPH: 2.07 | KPH: 6.12
  - `Werkstundent` + `Car`: 8.0 h (0.2%) | Cost: 21.79 EUR/h | TPH: 1.25 | KPH: 4.65
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Neuss
- **Ore active în Mai**: 282.00 h
- **Cost mediu orar actual**: **25.81 EUR/h** (Depășește pragul cu **3.31 EUR/h**)
- **TPH mediu actual**: 1.39 livrări/h | **KPH mediu actual**: 9.47 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 2.0 h (0.7%) | Cost: 28.82 EUR/h | TPH: 1.50 | KPH: 12.03
  - `TZ` + `Bicycle`: 14.0 h (5.0%) | Cost: 24.59 EUR/h | TPH: 1.29 | KPH: 10.05
  - `TZ` + `Car`: 266.0 h (94.3%) | Cost: 25.85 EUR/h | TPH: 1.39 | KPH: 9.42
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Worms
- **Ore active în Mai**: 879.00 h
- **Cost mediu orar actual**: **25.77 EUR/h** (Depășește pragul cu **3.27 EUR/h**)
- **TPH mediu actual**: 1.74 livrări/h | **KPH mediu actual**: 7.74 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 62.0 h (7.1%) | Cost: 24.55 EUR/h | TPH: 1.66 | KPH: 5.09
  - `Minijob` + `Car`: 444.0 h (50.5%) | Cost: 27.01 EUR/h | TPH: 1.78 | KPH: 8.36
  - `TZ` + `Car`: 318.0 h (36.2%) | Cost: 24.98 EUR/h | TPH: 1.72 | KPH: 7.55
  - `Werkstundent` + `Bicycle`: 55.0 h (6.3%) | Cost: 21.74 EUR/h | TPH: 1.55 | KPH: 6.83
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Fuerth
- **Ore active în Mai**: 1,657.00 h
- **Cost mediu orar actual**: **25.74 EUR/h** (Depășește pragul cu **3.24 EUR/h**)
- **TPH mediu actual**: 1.74 livrări/h | **KPH mediu actual**: 9.53 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 1.0 h (0.1%) | Cost: 25.40 EUR/h | TPH: 1.00 | KPH: 7.68
  - `Minijob` + `Car`: 218.0 h (13.2%) | Cost: 27.46 EUR/h | TPH: 1.56 | KPH: 9.27
  - `TZ` + `Bicycle`: 230.0 h (13.9%) | Cost: 23.80 EUR/h | TPH: 1.86 | KPH: 7.50
  - `TZ` + `Car`: 1075.0 h (64.9%) | Cost: 26.35 EUR/h | TPH: 1.73 | KPH: 10.49
  - `Werkstundent` + `Bicycle`: 133.0 h (8.0%) | Cost: 21.41 EUR/h | TPH: 1.93 | KPH: 5.66
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Berlin
- **Ore active în Mai**: 35,650.99 h
- **Cost mediu orar actual**: **25.52 EUR/h** (Depășește pragul cu **3.02 EUR/h**)
- **TPH mediu actual**: 2.02 livrări/h | **KPH mediu actual**: 9.72 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 2159.0 h (6.1%) | Cost: 25.05 EUR/h | TPH: 2.02 | KPH: 6.61
  - `Minijob` + `Car`: 1710.0 h (4.8%) | Cost: 28.34 EUR/h | TPH: 1.95 | KPH: 11.07
  - `TZ` + `Bicycle`: 6852.0 h (19.2%) | Cost: 23.50 EUR/h | TPH: 1.93 | KPH: 6.53
  - `TZ` + `Car`: 19912.0 h (55.9%) | Cost: 27.02 EUR/h | TPH: 2.04 | KPH: 11.94
  - `Werkstundent` + `Bicycle`: 5012.0 h (14.1%) | Cost: 21.55 EUR/h | TPH: 2.06 | KPH: 6.16
  - `Werkstundent` + `Car`: 6.0 h (0.0%) | Cost: 22.78 EUR/h | TPH: 1.17 | KPH: 6.98
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Tranziție către Biciclete (Congestie urbană)**: Deoarece Berlin are o congestie ridicată (Frankfurt/München au blocaje masive în centru), viteza mașinilor este redusă iar timpul de parcare este mare. BTPH (TPH pe bicicletă) este istoric mai mare sau egal cu cel auto în centru. Se recomandă înlocuirea mașinilor cu biciclete electrice în proporție de **80% biciclete / 20% mașini** pentru livrările ultra-centrale.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Muenster
- **Ore active în Mai**: 50.00 h
- **Cost mediu orar actual**: **25.49 EUR/h** (Depășește pragul cu **2.99 EUR/h**)
- **TPH mediu actual**: 1.50 livrări/h | **KPH mediu actual**: 7.61 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 15.0 h (30.0%) | Cost: 26.30 EUR/h | TPH: 1.20 | KPH: 6.92
  - `TZ` + `Car`: 35.0 h (70.0%) | Cost: 25.15 EUR/h | TPH: 1.63 | KPH: 7.90
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Potsdam
- **Ore active în Mai**: 3,248.00 h
- **Cost mediu orar actual**: **25.41 EUR/h** (Depășește pragul cu **2.91 EUR/h**)
- **TPH mediu actual**: 1.89 livrări/h | **KPH mediu actual**: 9.82 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 89.0 h (2.7%) | Cost: 25.56 EUR/h | TPH: 1.63 | KPH: 8.15
  - `Minijob` + `Car`: 328.0 h (10.1%) | Cost: 29.23 EUR/h | TPH: 2.18 | KPH: 12.87
  - `TZ` + `Bicycle`: 484.0 h (14.9%) | Cost: 23.48 EUR/h | TPH: 1.83 | KPH: 6.47
  - `TZ` + `Car`: 1646.0 h (50.7%) | Cost: 26.65 EUR/h | TPH: 1.86 | KPH: 11.15
  - `Werkstundent` + `Bicycle`: 701.0 h (21.6%) | Cost: 22.03 EUR/h | TPH: 1.91 | KPH: 7.82
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Oberhausen
- **Ore active în Mai**: 255.00 h
- **Cost mediu orar actual**: **25.15 EUR/h** (Depășește pragul cu **2.65 EUR/h**)
- **TPH mediu actual**: 1.42 livrări/h | **KPH mediu actual**: 8.00 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `TZ` + `Bicycle`: 9.0 h (3.5%) | Cost: 23.87 EUR/h | TPH: 1.11 | KPH: 7.72
  - `TZ` + `Car`: 246.0 h (96.5%) | Cost: 25.19 EUR/h | TPH: 1.43 | KPH: 8.01
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Menținerea interdicției pe Minijobs**: Nu se vor aproba contracte noi de tip Minijob în acest oraș.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Reutlingen
- **Ore active în Mai**: 492.00 h
- **Cost mediu orar actual**: **25.14 EUR/h** (Depășește pragul cu **2.64 EUR/h**)
- **TPH mediu actual**: 1.71 livrări/h | **KPH mediu actual**: 7.89 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `TZ` + `Car`: 492.0 h (100.0%) | Cost: 25.14 EUR/h | TPH: 1.71 | KPH: 7.89
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Menținerea interdicției pe Minijobs**: Nu se vor aproba contracte noi de tip Minijob în acest oraș.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Moers
- **Ore active în Mai**: 137.00 h
- **Cost mediu orar actual**: **25.09 EUR/h** (Depășește pragul cu **2.59 EUR/h**)
- **TPH mediu actual**: 1.55 livrări/h | **KPH mediu actual**: 5.95 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 91.0 h (66.4%) | Cost: 24.79 EUR/h | TPH: 1.54 | KPH: 5.80
  - `Minijob` + `Car`: 40.0 h (29.2%) | Cost: 25.81 EUR/h | TPH: 1.65 | KPH: 5.93
  - `TZ` + `Bicycle`: 2.0 h (1.5%) | Cost: 23.74 EUR/h | TPH: 1.00 | KPH: 7.31
  - `TZ` + `Car`: 4.0 h (2.9%) | Cost: 25.52 EUR/h | TPH: 1.00 | KPH: 8.71
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Hagen
- **Ore active în Mai**: 141.00 h
- **Cost mediu orar actual**: **24.98 EUR/h** (Depășește pragul cu **2.48 EUR/h**)
- **TPH mediu actual**: 1.23 livrări/h | **KPH mediu actual**: 7.73 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 2.0 h (1.4%) | Cost: 26.87 EUR/h | TPH: 1.00 | KPH: 8.10
  - `TZ` + `Bicycle`: 11.0 h (7.8%) | Cost: 24.30 EUR/h | TPH: 1.00 | KPH: 9.13
  - `TZ` + `Car`: 128.0 h (90.8%) | Cost: 25.01 EUR/h | TPH: 1.25 | KPH: 7.61
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Gelsenkirchen
- **Ore active în Mai**: 654.00 h
- **Cost mediu orar actual**: **24.81 EUR/h** (Depășește pragul cu **2.31 EUR/h**)
- **TPH mediu actual**: 1.50 livrări/h | **KPH mediu actual**: 7.21 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 6.0 h (0.9%) | Cost: 26.66 EUR/h | TPH: 1.33 | KPH: 7.66
  - `TZ` + `Bicycle`: 24.0 h (3.7%) | Cost: 23.23 EUR/h | TPH: 1.42 | KPH: 5.65
  - `TZ` + `Car`: 624.0 h (95.4%) | Cost: 24.85 EUR/h | TPH: 1.50 | KPH: 7.26
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Hamm
- **Ore active în Mai**: 63.00 h
- **Cost mediu orar actual**: **24.68 EUR/h** (Depășește pragul cu **2.18 EUR/h**)
- **TPH mediu actual**: 1.13 livrări/h | **KPH mediu actual**: 6.89 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `TZ` + `Car`: 63.0 h (100.0%) | Cost: 24.68 EUR/h | TPH: 1.13 | KPH: 6.89
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Menținerea interdicției pe Minijobs**: Nu se vor aproba contracte noi de tip Minijob în acest oraș.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Harburg
- **Ore active în Mai**: 68.00 h
- **Cost mediu orar actual**: **24.63 EUR/h** (Depășește pragul cu **2.13 EUR/h**)
- **TPH mediu actual**: 1.32 livrări/h | **KPH mediu actual**: 6.50 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 6.0 h (8.8%) | Cost: 25.81 EUR/h | TPH: 1.33 | KPH: 5.93
  - `TZ` + `Car`: 62.0 h (91.2%) | Cost: 24.52 EUR/h | TPH: 1.32 | KPH: 6.56
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Erlangen
- **Ore active în Mai**: 1,034.00 h
- **Cost mediu orar actual**: **24.37 EUR/h** (Depășește pragul cu **1.87 EUR/h**)
- **TPH mediu actual**: 2.02 livrări/h | **KPH mediu actual**: 7.37 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 103.0 h (10.0%) | Cost: 24.66 EUR/h | TPH: 1.70 | KPH: 5.41
  - `Minijob` + `Car`: 212.0 h (20.5%) | Cost: 28.55 EUR/h | TPH: 2.08 | KPH: 11.48
  - `TZ` + `Bicycle`: 483.0 h (46.7%) | Cost: 23.47 EUR/h | TPH: 2.14 | KPH: 6.44
  - `TZ` + `Car`: 47.0 h (4.5%) | Cost: 26.03 EUR/h | TPH: 1.91 | KPH: 9.81
  - `Werkstundent` + `Bicycle`: 189.0 h (18.3%) | Cost: 21.39 EUR/h | TPH: 1.81 | KPH: 5.59
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Leipzig
- **Ore active în Mai**: 3,001.00 h
- **Cost mediu orar actual**: **24.33 EUR/h** (Depășește pragul cu **1.83 EUR/h**)
- **TPH mediu actual**: 1.48 livrări/h | **KPH mediu actual**: 6.30 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 79.0 h (2.6%) | Cost: 26.26 EUR/h | TPH: 1.47 | KPH: 6.84
  - `TZ` + `Bicycle`: 189.0 h (6.3%) | Cost: 22.64 EUR/h | TPH: 1.57 | KPH: 3.74
  - `TZ` + `Car`: 2635.0 h (87.8%) | Cost: 24.53 EUR/h | TPH: 1.48 | KPH: 6.58
  - `Werkstundent` + `Bicycle`: 98.0 h (3.3%) | Cost: 20.77 EUR/h | TPH: 1.47 | KPH: 3.42
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Aschaffenburg
- **Ore active în Mai**: 405.00 h
- **Cost mediu orar actual**: **24.20 EUR/h** (Depășește pragul cu **1.70 EUR/h**)
- **TPH mediu actual**: 1.39 livrări/h | **KPH mediu actual**: 5.87 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `TZ` + `Car`: 405.0 h (100.0%) | Cost: 24.20 EUR/h | TPH: 1.39 | KPH: 5.87
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Menținerea interdicției pe Minijobs**: Nu se vor aproba contracte noi de tip Minijob în acest oraș.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Krefeld
- **Ore active în Mai**: 149.00 h
- **Cost mediu orar actual**: **24.16 EUR/h** (Depășește pragul cu **1.66 EUR/h**)
- **TPH mediu actual**: 1.34 livrări/h | **KPH mediu actual**: 5.12 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Car`: 29.0 h (19.5%) | Cost: 25.55 EUR/h | TPH: 1.52 | KPH: 5.42
  - `TZ` + `Car`: 120.0 h (80.5%) | Cost: 23.82 EUR/h | TPH: 1.30 | KPH: 5.05
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Duisburg
- **Ore active în Mai**: 893.00 h
- **Cost mediu orar actual**: **23.73 EUR/h** (Depășește pragul cu **1.23 EUR/h**)
- **TPH mediu actual**: 1.66 livrări/h | **KPH mediu actual**: 5.83 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `Minijob` + `Bicycle`: 4.0 h (0.4%) | Cost: 24.57 EUR/h | TPH: 1.00 | KPH: 5.16
  - `Minijob` + `Car`: 10.0 h (1.1%) | Cost: 27.56 EUR/h | TPH: 1.10 | KPH: 9.49
  - `TZ` + `Bicycle`: 422.0 h (47.3%) | Cost: 23.50 EUR/h | TPH: 1.60 | KPH: 6.54
  - `TZ` + `Car`: 457.0 h (51.2%) | Cost: 23.84 EUR/h | TPH: 1.73 | KPH: 5.10
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Eliminarea Minijobs**: Concedierea sau conversia tuturor angajaților cu Minijob (care costă > 25 EUR/h) către Werkstudent pe bicicletă.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

### Iserlohn
- **Ore active în Mai**: 77.00 h
- **Cost mediu orar actual**: **23.48 EUR/h** (Depășește pragul cu **0.98 EUR/h**)
- **TPH mediu actual**: 1.39 livrări/h | **KPH mediu actual**: 6.38 km/h
- **Structura actuală a contractelor/vehiculelor active**:
  - `TZ` + `Bicycle`: 75.0 h (97.4%) | Cost: 23.44 EUR/h | TPH: 1.40 | KPH: 6.34
  - `TZ` + `Car`: 2.0 h (2.6%) | Cost: 25.13 EUR/h | TPH: 1.00 | KPH: 7.87
- **Pași clari de eficientizare pentru a atinge maximum 22.50 EUR/oră**:
  1. **Menținerea interdicției pe Minijobs**: Nu se vor aproba contracte noi de tip Minijob în acest oraș.
  2. **Restructurarea Teilzeit (TZ)**: Stoparea recrutării TZ. Angajații TZ existenți pe mașină trebuie transferați pe Werkstudent pe bicicletă sau supuși politicii de căpuire a kilometrilor (Plan B).
  3. **Optimizarea Flotei Auto/Bicicletă**: Menținerea mașinilor doar sub contracte Werkstudent cu aplicarea strictă a limitei de kilometri (Plan B) și limitarea geografică a curselor.
  4. **Recrutare pentru Vârful de Vară**: Suplinirea deficitului de capacitate din iunie prin angajarea de Werkstudenten permanent și studenți pe contract sezonier (Kurzfristig) pe bicicletă, asigurând costuri orare de ~17.00 - 21.00 EUR.

________________________________________

---

## 5. Strategia de Comision Progresiv / Tiered (Grupare Forfetară)

Pentru a preveni pierderile cauzate de șoferii cu TPH scăzut (care fac 11-12h și doar 1 comandă pe oră, generând costuri mari cu kilometrii fără venituri), propunem implementarea unui **comision progresiv** (flat-rate tiered commission) aplicat la nivel de driver-week pe Umsatzul realizat în aplicație:

| Prag Umsatz Săptămânal | Commission % (Luată de noi) | Commission % (Rămasă la Driver) | Explicație Financiară | Impact Asupra Șoferului |
| :--- | :--- | :--- | :--- | :--- |
| **< 400 EUR** | **8.0%** | 92.0% | Șoferi cu productivitate slabă / Minijobs sporadici. Acoperă doar costurile minime. | Povară mică, nu descurajează începătorii. |
| **400 - 800 EUR** | **10.0%** | 90.0% | Productivitate medie (~10-20h/săptămână). Începe să compenseze riscul de kilometri. | Acceptabil, crește implicarea șoferului. |
| **800 - 1200 EUR** | **12.0%** | 88.0% | Productivitate ridicată (~20-35h). Acoperă complet riscurile operaționale. | Echitabil, corelat cu volumul mare de livrări. |
| **> 1200 EUR** | **15.0%** | 85.0% | Șoferi profesioniști / Full-time (ture lungi). Protejează compania împotriva costurilor de rulaj mare. | Rezonabil, șoferul câștigă oricum o sumă netă mare. |


### Analiza impactului pe date reale (Mai):
- În Mai, am realizat un Umsatz total de **2,774,019.23 EUR**.
- Sub comisionul standard de 8%, veniturile noastre din comisioane au fost de **221,921.54 EUR**, în timp ce am plătit **377,686.02 EUR** în decontări de kilometri, rezultând o pierdere netă de **155,764.48 EUR** doar pe partea de rulaj orar pe contracte din cauza decontării nelimitate de kilometri.
- Prin aplicarea **Comisionului Progresiv Tiered**, veniturile din comisioane cresc la **288,095.80 EUR** (o creștere directă de **66,174.27 EUR** de profit orar, fără a afecta șoferii cu venituri mici).

---

## 6. Simularea Politicii de Căpuire a Kilometrilor pe Contracte (Abordare de Tip Gewerbe)

Sub această abordare, deși curierii noștri sunt angajați strict cu contracte de muncă standard (cu toate taxele sociale achitate), aplicăm o regulă internă de tip *Gewerbe* pentru decontarea kilometrilor în scopul responsabilizării acestora. Kilometrii sunt decontați în mod normal (0.20 EUR/km bike, 0.30 EUR/km car), dar compensația este suspendată sau capată dacă activitatea lor ne duce pe minus.

Pentru a preveni pierderile când comisionul reținut este mai mic decât kilometrii decontați, am simulat două politici interne pe baza celor 8,346 driver-weeks active în Mai:

- **Politica A (Tăiere drastică)**: Nu se plătesc kilometri deloc în săptămânile în care comisionul obținut de la șofer este mai mic decât kilometrii decontați (intram pe minus).
  - **Impact**: Economisim **371,967.59 EUR** la nivel de lună. Plata totală de kilometri scade la doar 5,718.43 EUR. Profitul nostru net din comisioane devine **+216,203.11 EUR**.
  - *Atenție*: Această politică poate fi o povară prea mare pentru șoferi și poate cauza plecări masive din flotă.

- **Politica B (Capare la Breakeven - Recomandată)**: Kilometrii plătiți șoferului sunt capabili la valoarea comisionului generat de el pe acea săptămână (astfel încât profitul pe acel șofer să fie cel puțin 0).
  - **Impact**: Economisim **156,899.47 EUR**. Plata totală de kilometri scade la 220,786.55 EUR, iar profitul nostru net din comisioane devine **+1,134.98 EUR** (trecem pe zero/breakeven, eliminând complet pierderile pe fiecare șofer).
  - *Impact cumulat cu comisionul progresiv (Tiered)*: Dacă combinăm **Comisionul Progresiv + Căparea Kilometrilor (Politica B)**, obținem un profit net garantat de **+7,590.87 EUR** pe lună, iar șoferii primesc decontări mai mari (plata totală de km crește la 280,504.93 EUR), asigurând retenția flotei.

---

## 7. Berlin: Strategia de Sezonier (Kurzfristige Beschäftigung)

În Berlin, avem o masă mare de studenți disponibili. Strategia propusă constă în angajarea lor inițială pe o perioadă de maximum 3 luni (sezonieri / Kurzfristige Beschäftigung) în timpul vacanței de vară.

### Argumente Matematice:
1. **Reducerea Taxelor**: Taxele angajatorului scad de la 31.89% (Werkstudent) la **3.00%** (levier de accident, insolvență și U1/U2).
2. **Calculul de Cost pe Bicicletă (KPH mediu în Berlin = 6.16 km/h)**:
   - Werkstudent + Bicicletă:  
     $$(13.90 + 6.16 \times 0.20) \times 1.3189 \times 1.08 = \mathbf{21.55 \text{ EUR/oră}}$$ (Prag respectat, profit limitat)
   - Sezonier (Kurzfristig 3% taxă) + Bicicletă:  
     $$(13.90 + 6.16 \times 0.20) \times 1.03 \times 1.08 = \mathbf{16.85 \text{ EUR/oră}}$$ (Economisire de **4.70 EUR/oră** per angajat!)
3. **Calculul de Cost pe Mașină (KPH mediu în Berlin = 10.27 km/h)**:
   - Werkstudent + Mașină:  
     $$(13.90 + 10.27 \times 0.30) \times 1.3189 \times 1.08 = \mathbf{24.18 \text{ EUR/oră}}$$ (Depășește pragul de 22.50 EUR)
   - Sezonier (Kurzfristig 3% taxă) + Mașină:  
     $$(13.90 + 10.27 \times 0.30) \times 1.03 \times 1.08 = \mathbf{18.91 \text{ EUR/oră}}$$ (Pe deplin conform sub limita de 22.50 EUR!)

Această strategie ne oferă o flexibilitate uriașă în Berlin, permițându-ne să utilizăm chiar și mașini pe timp de vară sub pragul de 22.50 EUR/oră.

---

## 8. Strategia pentru Vârful de Sezon din Vară (Săptămânile 5-10)

Pe baza datelor de forecast din iunie (săptămânile 1-5 din fișierele specifice), observăm o creștere masivă a comenzilor în ultimele săptămâni (W4 și W5):
- **Berlin**: crește de la 8.5k (W1) la 13.8k (W5) - **+61.7%**
- **München**: crește de la 7.0k (W1) la 11.4k (W5) - **+61.7%**
- **Frankfurt**: crește de la 5.3k (W1) la 8.5k (W5) - **+61.5%**
- **Leipzig**: crește de la 870 (W1) la 2,077 (W5) - **+138.7%**

În paralel, estimăm că **25-30% din șoferii activi existenți vor pleca în concediu**.

### Plan de acțiune pentru acoperirea cererii în siguranță financiară:
1. **Recrutare Targetată**: Activarea imediată a campaniilor de recrutare în universități pentru contracte de tip **Werkstudent pe bicicletă** și **Kurzfristige Beschäftigung (sezonier) pe bicicletă**.
2. **Corelarea cu Dashboard-ul de Forecast**: Corelarea necesarului zilnic cu orele de vârf (prânz: 11:30 - 13:30 și seară: 18:00 - 21:00) unde cererea este maximă, pentru a evita menținerea șoferilor activi în afara orelor de vârf, unde TPH-ul lor scade sub breakeven-ul de 2.25.
3. **Stimulente pentru șoferii activi**: Implementarea de bonusuri de performanță bazate pe TPH, finanțate din surplusul obținut din comisionul progresiv pe șoferii cu comenzi mari, stimulând șoferii să rămână activi în weekend-urile de vară în loc să plece în concediu.