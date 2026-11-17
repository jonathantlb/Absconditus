# Absconditus 

# 

# 📖 Manual Consolidado de Regras do Sistema





> \*\*Status do Documento:\*\* Compilado e Corrigido após Auditoria do Ecossistema de Regras.
>
> \*\*Finalidade:\*\* referência técnica definitiva para ficha, Mestre, aplicação digital e futuras implementações.
>
> \*\*Hierarquia:\*\* `REGRAS-CONSOLIDADAS` prevalece sobre regras conflitantes de versões anteriores; o `Livro de Magias Superno` prevalece para estrutura mágica e matriz; `Armas e Itens` prevalece para arsenal, organizações e armas lendárias. Guias antigos/protótipos são apenas referência histórica.





\---





## 🔍 1. Relatório de Incoerências e Correções Aplicadas

### 1.1 Limite de Magias × Progressão de Slots



**Conflito:** versões do Livro de Magias indicam 6 slots no Rank S e progressões que podem resultar em mais magias acumuladas. `REGRAS-CONSOLIDADAS` fixa o limite total em **1/2/3/4/5/5**.





**Regra definitiva:**



|Rank|Limite total de magias conhecidas|
|-|-:|
|E|1|
|D|2|
|C|3|
|B|4|
|A|5|
|S|6|





O limite é **total**, não por elemento. Ao subir de Rank, as magias anteriores são preservadas dentro do novo limite; novas magias podem ocupar os espaços disponíveis. Magias de Rank inferior continuam utilizáveis. Troca de magia depende de autorização verbal do Mestre.



**Distribuição elemental:** o número de afinidades é independente do número de magias. O personagem pode possuir até **3 afinidades elementais**, mas conhecer uma afinidade não libera todas as magias dela. B/A dão acesso às Evoluções; S pode trabalhar com até três afinidades, sempre respeitando o limite de 5 magias conhecidas.





### 1.2 HP e SAN — Fórmulas de Atributos × Tabelas



Uma versão de `Armas e Itens` utiliza fórmulas antigas como `HP = 10 + Força×2 + Resistência` e `SAN = 30 + Inteligência×2 + Determinação×2`. Essas fórmulas **não são o método oficial de recursos**.



O método soberano é aditivo:

```text
HP Máximo = Base HP do Rank + Mod. Classe + Mod. Raça
Proteção = Base Proteção do Rank + Mod. Classe + Mod. Raça
SAN Máxima = Base SAN do Rank + Mod. Classe + Mod. Raça + bônus de itens
```



Ao mudar Rank, Classe ou Raça, os máximos são recalculados. Pontos manuais de Atributos permanecem. Ao trocar Classe, remove-se o modificador antigo antes de aplicar o novo. Se um máximo diminuir abaixo do valor atual, o atual é limitado ao novo máximo; se aumentar, o atual **não** é restaurado automaticamente.



**Exemplo:** Atirador + Vampiro + Rank D = `HP 50+5+5 = 60`, `Proteção 25+2+3 = 30`, `SAN 55+5+5 = 65`.



### 1.3 Proteção Permanente × Temporária



A **Proteção permanente** vem do uniforme principal da Organização e segue o Rank:



|Rank|Proteção|
|-|-:|
|E|20|
|D|25|
|C|30|
|B|35|
|A|40|
|S|45|



Magias e efeitos podem conceder **Proteção Temporária**, que não altera a Proteção permanente e é consumida primeiro.

```text
Dano → Proteção Temporária → Proteção Permanente → HP
```

Dano mágico segue a mesma ordem, salvo descrição expressa em contrário. Sangramento ignora ambas.



### 1.4 Teste de Ação D20



O Livro de Magias trazia `D20 ≤ 10` como regra simplificada. A regra consolidada substitui essa leitura:



|D20|Resultado|
|-:|-|
|1|Falha Crítica|
|2–9|Falha|
|10–19|Sucesso Comum|
|20|Sucesso Crítico|



Não existe uma segunda rolagem defensiva automática do alvo de uma magia.



### 1.5 Sangramento



Crítico natural 20 com armas cortantes, perfurantes ou armas de fogo aplica **1D4/turno**, ignorando Proteção e indo diretamente ao HP. O efeito acumula até **2D4**. O dano de Sangramento não recebe Atributo nem Habilidade. Tratamento: Medicina CD 12 ou Kit Médico CD 10.



Em armas lendárias, o crítico especificado como 2D4 continua respeitando o teto geral de 2D4.



### 1.6 Dados de Magia — Correção de Fórmulas Antigas



O Livro atual possui cabeçalho de progressão por Rank, mas versões antigas contêm magias com fórmulas incompatíveis. Para implementação, o dado é determinado pelo Rank:



|Rank|SAN|Dado base|
|-|-:|-|
|E|5|`1D6 + Superno`|
|D|10|`2D6 + Superno`|
|C|15|`3D6 + Superno`|
|B|20|`4D6 + Superno`|
|A|25|`5D6 + Superno`|
|S|35|`6D6 + Superno`|



Uma entrada antiga que contradiga o dado do próprio Rank deve ser tratada como erro de transcrição.

### 1.7 Matriz Elemental



A matriz definitiva possui **12 entradas**: seis Primários + seis Evoluções.

**Primários:** Água, Fogo, Terra, Ar, Luz, Trevas.

**Evoluções:** Água→Gelo; Fogo→Plasma; Terra→Metal; Ar→Raio; Luz→Luz Intensificada; Trevas→Trevas Intensificadas.

Os nomes antigos **Vento** e **Relâmpago** foram substituídos por **Ar** e **Raio**. Natureza, Celestial e Sangue não pertencem à matriz atual.

### 

### 1.8 Mikazuki-Munechika



Há referência histórica a museu/exposição e, simultaneamente, ao estado de desaparecida. Para a continuidade do RPG, a regra narrativa é: **Mikazuki-Munechika está desaparecida no universo Absconditus**. A localização é determinada pela campanha; referências históricas são apenas contexto.





\---





## 🎲 2. Resolução de Testes e Combate

### 2.1 D20



```text
1 = Falha Crítica
2–9 = Falha
10–19 = Sucesso Comum
20 = Sucesso Crítico


```



### 2.2 Ataque e Dano Físico



```text
Dano = Dados da Arma + Atributo + Habilidade
```





|Uso|Atributo|
|-|-|
|Longo alcance|Precisão|
|Espadas/lâminas|Destreza|
|Força física|Força|
|Movimento/iniciativa|Agilidade|
|Medicina|Inteligência|
|Magia, exorcismo e selamento|Superno|

### 

### 2.3 Sangramento



`1D4/turno`, máximo `2D4`, direto no HP e ignorando Proteção. Tratamento: Medicina CD 12 ou Kit Médico CD 10.



### 2.4 Proteção



Proteção Temporária é consumida antes da Proteção Permanente. Dano crítico principal passa primeiro pela Proteção; somente o Sangramento posterior ignora Proteção.





\---





## 📊 3. Atributos, Classes, Raças e Progressão



### 3.1 Atributos



Escala principal: **0 a 10**. Rank E começa com zero pontos manuais e recebe a influência da Classe. Cada promoção concede **+2 pontos manuais**. Não existe queda de Rank.



### 3.2 Bônus de Classe



|Classe|Atributos|
|-|-|
|Caçador|Força +2 / Percepção +2|
|Atirador|Precisão +2 / Agilidade +2|
|Espadachim|Destreza +2 / Precisão +2|
|Sacerdote|Superno +2 / Inteligência +2|
|Feiticeiro|Percepção +2 / Destreza +2|
|Bruxo|Inteligência +2 / Superno +2|
|Investigador|Agilidade +2 / Destreza +2|

### 



### 3.3 Base por Rank



|Rank|HP|Proteção|SAN|
|-|-:|-:|-:|
|E|40|20|45|
|D|50|25|55|
|C|60|30|65|
|B|70|35|75|
|A|80|40|85|
|S|90|45|95|

### 



### 3.4 Modificadores por Classe



|Classe|HP|Proteção|SAN|
|-|-:|-:|-:|
|Caçador|+10|+2|-5|
|Atirador|+5|+2|+5|
|Espadachim|+5|+2|+0|
|Sacerdote|+0|+1|+10|
|Feiticeiro|+0|+0|+10|
|Bruxo|+0|+1|+15|
|Investigador|+0|+1|+5|

### 



### 3.5 Modificadores por Raça



|Raça|HP|Proteção|SAN|
|-|-:|-:|-:|
|Humano|+0|+0|+0|
|Vampiro|+5|+3|+5|
|Licantropo|+10|+2|-5|
|Celestial|+0|+2|+10|
|Demônio|+5|+1|+0|
|Híbrido|+5|+2|+5|

### 

### 3.6 Fórmulas



```text


HP = Base HP do Rank + Classe + Raça
Proteção = Base Proteção do Rank + Classe + Raça
SAN = Base SAN do Rank + Classe + Raça + bônus de itens


```



Nenhum recurso permanente ultrapassa seu máximo. Alterações de Classe/Raça/Rank recalculam os máximos; o valor atual só é reduzido automaticamente quando exceder o novo máximo.





\---





## 🧙‍♂️ 4. Sistema Místico, Magias e Elementos

### 4.1 Conjuração





```text
Dados da Magia + Superno
```



O custo de SAN é descontado imediatamente ao conjurar, mesmo se o teste falhar. Sem SAN suficiente, a conjuração é bloqueada. A mesma ação não pode descontar SAN duas vezes.





### 4.2 Rank, SAN e Dados



|Rank|Custo|Dado|
|-|-:|-|
|E|5 SAN|`1D6 + Superno`|
|D|10 SAN|`2D6 + Superno`|
|C|15 SAN|`3D6 + Superno`|
|B|20 SAN|`4D6 + Superno`|
|A|25 SAN|`5D6 + Superno`|
|S|35 SAN|`6D6 + Superno`|

### 



### 4.3 Magias Conhecidas



|Rank|Limite|
|-|-:|
|E|1|
|D|2|
|C|3|
|B|4|
|A|5|
|S|5|





O personagem pode usar magia de seu Rank ou inferior.



### 4.4 Afinidades



Até **3 afinidades elementais**. Conhecer uma afinidade não libera automaticamente suas magias.





### 4.5 Primários e Evoluções



|Primário|Evolução|
|-|-|
|Água|Gelo|
|Fogo|Plasma|
|Terra|Metal|
|Ar|Raio|
|Luz|Luz Intensificada|
|Trevas|Trevas Intensificadas|



Cada Primário possui 11 magias na estrutura atual; cada Evolução possui 5: **3 Dano, 1 Suporte, 1 Controle**.





### 4.6 Alcances



|Alcance|Distância|
|-|-:|
|Toque|1m|
|Curto|10m|
|Médio|20m|
|Longo|40m|





Áreas devem indicar raio/geometria. Cura nunca ultrapassa HP máximo. Proteção temporária não altera a Proteção permanente.





### 4.7 Matriz Elemental



|Ataque \\ Defesa|Fogo|Plasma|Água|Gelo|Terra|Metal|Ar|Raio|Luz|Luz Intensificada|Trevas|Trevas Intensificadas|
|-|-|-|-|-|-|-|-|-|-|-|-|-|
|**Fogo**|—|—|V|V|V|V|N|N|D|D|D|D|
|**Plasma**|—|—|V|V|V|V|N|N|D|D|D|D|
|**Água**|D|D|—|—|V|V|V|V|N|N|D|D|
|**Gelo**|D|D|—|—|V|V|V|V|N|N|D|D|
|**Terra**|D|D|D|D|—|—|V|V|V|V|N|N|
|**Metal**|D|D|D|D|—|—|V|V|V|V|N|N|
|**Ar**|N|N|D|D|D|D|—|—|V|V|V|V|
|**Raio**|N|N|D|D|D|D|—|—|V|V|V|V|
|**Luz**|V|V|N|N|D|D|D|D|—|—|V|V|
|**Luz Intensificada**|V|V|N|N|D|D|D|D|—|—|V|V|
|**Trevas**|V|V|V|V|N|N|D|D|D|D|—|—|
|**Trevas Intensificadas**|V|V|V|V|N|N|D|D|D|D|—|—|





`V = +1D6`; `D = -1D6`; `N = neutro`; `— = mesma família`. O modificador não altera o `+ Superno` e o resultado não cai abaixo do mínimo do dado aplicável.

**Ciclo dos Primários:** `Fogo → Água → Terra → Ar → Luz → Trevas → Fogo`. Cada Primário é forte contra os dois seguintes e fraco contra os dois anteriores; Evoluções repetem o perfil de origem.





\---





## ⚔️ 5. Arsenais, Equipamentos e Organizações

### 5.1 Armas Brancas



|Arma|Porte|Dano|Atributo|Regra|
|-|-|-:|-|-|
|Katana|Média|2D6|Destreza|Sangramento no crítico 20|
|Espada reta|Média|2D6|Destreza|Sangramento no crítico 20|
|Rapieira|Média|2D6|Destreza|Estocadas; Sangramento no crítico 20|
|Machado 1 mão|Grande|2D6+1|Força|Sangramento no crítico 20|
|Machado 2 mãos|Muito grande|3D6|Força|Duas mãos; Sangramento no crítico 20|
|Faca|Leve|1D6|Destreza|Sangramento no crítico 20|
|Adaga|Leve|1D6+1|Destreza|Sangramento no crítico 20|
|Estrelas ninja|Leve|1D6|Destreza|Arremesso usa Precisão|
|Arco \& Flecha|Médio|2D6|Precisão|Longo alcance; Sangramento no crítico 20|
|Bastão curto|Médio|1D6+1|Força|Contundente; sem Sangramento|
|Bastão longo|Grande|2D6|Força|Contundente; sem Sangramento|
|Corrente/Chicote|Médio|1D6+1|Destreza|Pode desarmar conforme Mestre|

### 

### 

### 5.2 Armas de Fogo



|Arma|Dano|Atributo|Observação|
|-|-:|-|-|
|Pistola|2D6|Precisão|Sangramento no crítico 20|
|SMG|2D6+1|Precisão|Curto/médio alcance|
|Rifle de assalto|3D6|Precisão|Médio/longo alcance|
|Rifle de precisão|4D6|Precisão|Longo alcance|

### 

### 

### 5.3 Granadas



|Item|Raio|Efeito|
|-|-:|-|
|Fragmentação|4m|`3D6`; aliados fazem Agilidade CD 14 para meio dano|
|Luz|5m|Percepção CD 13; falha: cegueira 1 turno + -2 Precisão por 2 turnos|
|Fumaça|6m|Cobertura pesada por 3 turnos; ataques através sofrem Desvantagem; entrada exige Percepção CD 12|



Não usam SAN.





### 5.4 Itens Superno



|Item|Regra|
|-|-|
|Grimório/Tomo|+2 Superno em conjuração/ocultismo através dele|
|Varinha|+1D6 no efeito de uma magia por cena|
|Cajado|+3 Superno para uma magia de cura/proteção por cena|
|Anel|1 repetição de rolagem de efeito mágico por cena|
|Amuleto|+5 SAN máxima|

### 

### 

### 5.5 Erva do Véu



`+20 SAN`, limitada à SAN máxima. Após duas na mesma cena, cada adicional recupera `+5 SAN`. Em três cenas consecutivas, a próxima também recupera `+5 SAN`; uma cena completa sem uso restaura a tolerância. Com tolerância ativa, falha crítica pode exigir teste de Corrupção Leve.



### 5.6 Kit Médico



`+20 HP`, exigindo Habilidade Medicina.





### 5.7 Equipamento por Organização



|Organização|Equipamento padrão|
|-|-|
|Credo do Caçador|Machado 1 mão + Pistola|
|Centro de Observação|Pistola + Faca|
|Pax Vobiscum|Grimório/Tomo + Amuleto|
|Filhos da Terra|Varinha + Cajado|
|Ordem do Abismo|Grimório/Tomo + Adaga|
|A Divisão|Rifle de assalto + Pistola|
|Clã Akamatsu 赤松氏|Katana + Arco \& Flecha|
|Kurotsuki 黒月|Katana + Grimório/Tomo Marcado|



Ao escolher Organização, recebe duas armas/equipamentos, 2 Kits Médicos e 2 Ervas do Véu. Pode substituir uma das duas armas por uma única arma de outra Organização. Lendárias não podem ser escolhidas na criação.
Ao escolher sua Organização, o jogador recebe dois pontos de Habilidade que são inseridos da Árvore de Habilidades

# ABSconditus — Organização e Árvore de Habilidades

## Regra de criação de personagem

Ao escolher uma Organização, o personagem recebe:
- **2 armas/equipamentos**, conforme as opções da Organização;
- **2 Kits Médicos**;
- **2 Ervas do Véu**;
- **2 pontos de Habilidade** para distribuir na Árvore de Habilidades.

O personagem pode substituir **uma das duas armas/equipamentos iniciais** por **uma única arma de outra Organização**. **Armas Lendárias não podem ser escolhidas durante a criação.**

## Distribuição dos pontos

Cada Organização possui duas habilidades associadas às suas funções. Ao escolhê-la, o personagem recebe **+1 ponto em cada uma das duas habilidades indicadas**, totalizando 2 pontos.

Os pontos respeitam os limites máximos da Árvore de Habilidades. Se uma habilidade já estiver no limite, o ponto correspondente deve ser alocado em outra habilidade permitida pelo mestre. Esses pontos não substituem outros benefícios de criação.

## Organizações e habilidades associadas

| Organização | Função | Habilidade 1 | Habilidade 2 |
|---|---|---|---|
| **Credo do Caçador** | Combate · Eliminar ameaças | **Rastreamento +1** | **Arma de fogo +1** |
| **Centro de Observação** | Investigação · Compreender e registrar | **Investigação +1** | **Conhecimento +1** |
| **Pax Vobiscum** | Religião · Proteger e purificar | **Fé +1** | **Exorcismo +1** |
| **Filhos da Terra** | Natureza · Preservar o equilíbrio | **Afinidade +1** | **Selamento +1** |
| **Ordem do Abismo** | Magia sombria · Explorar o proibido | **Ocultismo +1** | **Superno +1** |
| **A Divisão** | Atiradores · Conter danos à sociedade | **Precisão +1** | **Arma de fogo +1** |
| **Clã Akamatsu 赤松氏** | Espadachins · Disciplina e domínio das lâminas | **Espadas +1** | **Reflexo +1** |
| **Kurotsuki 黒月** | Roubo · Contrabando de objetos Superno | **Furtividade +1** | **Ocultismo +1** |

## Justificativa das associações

### Credo do Caçador — Rastreamento e Arma de fogo
O Credo localiza, persegue e elimina ameaças Superno. Rastreamento representa a capacidade de encontrar alvos e seguir vestígios; Arma de fogo representa o treinamento de combate e a neutralização de ameaças.

### Centro de Observação — Investigação e Conhecimento
A organização coleta, analisa e registra ocorrências. Investigação permite encontrar e relacionar evidências; Conhecimento representa o repertório técnico, histórico e acadêmico necessário para interpretar os fenômenos.

### Pax Vobiscum — Fé e Exorcismo
A ordem atua por meio da religião, da proteção espiritual e da purificação. Fé representa convicção e vínculo religioso; Exorcismo representa a prática de expulsar ou afastar entidades e influências sobrenaturais.

### Filhos da Terra — Afinidade e Selamento
A organização procura preservar o equilíbrio e manter relações com as forças naturais do Superno. Afinidade representa conexão e sensibilidade diante dessas forças; Selamento representa a capacidade de conter ou estabilizar manifestações e ameaças.

### Ordem do Abismo — Ocultismo e Superno
A Ordem estuda e explora práticas mágicas proibidas. Ocultismo representa o conhecimento de rituais, símbolos e entidades; Superno representa a capacidade de lidar com a energia sobrenatural.

### A Divisão — Precisão e Arma de fogo
A Divisão atua com atiradores e operações de contenção. Precisão representa mira e acerto de alvos; Arma de fogo representa treinamento técnico e eficiência com armamentos de disparo.

### Clã Akamatsu — Espadas e Reflexo
O Clã valoriza disciplina e domínio das lâminas. Espadas representa técnica e manejo de armas cortantes; Reflexo representa reação, tempo de resposta e capacidade de acompanhar o ritmo de um duelo.

### Kurotsuki — Furtividade e Ocultismo
A Kurotsuki atua com roubo, contrabando e circulação clandestina de objetos Superno. Furtividade representa infiltração e movimentação discreta; Ocultismo representa a capacidade de reconhecer e compreender artefatos e objetos sobrenaturais.

---

## Referência — Árvore de Habilidades

Os nomes, grupos, limites e efeitos abaixo preservam a estrutura fornecida.

### CORPO

| Habilidade | Progressão / efeito |
|---|---|
| Força | 0/5 |
| Resistências | 0/20 |
| Rastreamento | 0/5 |
| Precisão | 0/5 |
| Arco | +2 dano/pt · 0/5 |
| Arma de fogo | +2 dano/pt · 0/5 |
| Espadas | +2 dano/pt · 0/5 |
| Reflexo | 0/5 |
| Artes Marciais | 0/5 |
| Furtividade | 0/5 |
| Pilotagem | 0/5 |

### MENTE

| Habilidade | Progressão / efeito |
|---|---|
| Conhecimento | 0/5 |
| Investigação | 0/5 |
| Hacker | 0/5 |
| Medicina | +5 HP/pt · 0/5 |
| Carisma | 0/5 |
| Liderança | 0/5 |

### ESPÍRITO

| Habilidade | Progressão / efeito |
|---|---|
| Superno | 0/5 |
| Fé | 0/5 |
| Exorcismo | 0/5 |
| Ocultismo | 0/5 |
| Afinidade | 0/5 |
| Selamento | 0/5 |
| Concentração | 0/5 |
| Determinação | 0/5 |

## Observações de balanceamento

1. **Dois pontos para todas as Organizações:** cada escolha concede exatamente dois pontos, mantendo o mesmo orçamento inicial.
2. **Especialização temática:** os pontos reforçam a função da Organização sem impedir o desenvolvimento de outras habilidades.
3. **Habilidades compartilhadas:** Arma de fogo aparece no Credo do Caçador e na Divisão porque ambas utilizam armamento de disparo. No Credo, a ênfase é a caça e neutralização de ameaças; na Divisão, a precisão e a contenção.
4. **Sem habilidades novas:** todas as associações utilizam habilidades já presentes na Árvore fornecida.
5. **Respeito aos limites:** os pontos concedidos pela Organização não ultrapassam o limite máximo de cada habilidade.

## Texto consolidado para o manual

> **Organização:** ao escolher uma Organização, o personagem recebe 2 armas/equipamentos, 2 Kits Médicos, 2 Ervas do Véu e 2 pontos de Habilidade. Esses pontos são distribuídos como +1 nas duas habilidades associadas à Organização escolhida. O personagem pode substituir uma das duas armas/equipamentos iniciais por uma única arma de outra Organização. Armas Lendárias não podem ser escolhidas durante a criação do personagem.






### 5.8 Kurotsuki



O Grimório Marcado fornece `+2 Superno`. Em magia Rank B+ através dele, role `1D6`; em **1**, um Coletor/entidade rastreadora percebe sua localização. Em 2–6, nada especial ocorre.





\---





## 🗡️ 6. Armas Superno Lendárias (Ranking S)



### Requisitos Gerais



Todas são Rank S e exigem:

```text
Superno 5
Habilidade da arma 5
SAN Máxima 40+
```

Com `SAN < 10`, o uso causa **1 Corrupção** conforme a regra geral das Lendárias.

No crítico natural 20, aplicam **2D4 Sangramento + efeito especial**, respeitando o teto geral de 2D4.

Se o usuário falhar em teste de SAN enquanto empunha uma Lendária, role 1D6: em 1, a arma assume controle por 1 turno narrado pelo Mestre.



### 6.1 Tentetsutou (天鉄刀)

* **Tipo:** Katana / Médio
* **Dano:** `4D6 + Superno + Espadas`
* **Custo:** 0 SAN passivo; 8 SAN para Sobrecarga de Meteorito.
* **Passivo — Condutor de Superno:** ignora 2 pontos de Resistência Espiritual contra dano Superno canalizado pela lâmina.
* **Ativo — Chuva de Ferro:** 1x/cena; por 8 SAN, converte o dano em dano Superno puro por 2 turnos e adiciona Superno novamente; depois, -2 Percepção por 1 cena.
* **Registro:** lâmina de meteorito associada a Vicky Tess.



### 6.2 Muramasa (村正)

* **Tipo:** Katana Amaldiçoada / Médio
* **Dano:** `5D6 + Destreza + Espadas`
* **Custo:** 5 SAN por turno em Fúria.
* **Passivo — Sede Incessante:** Sangramento automático em acerto; crítico permanece limitado a 2D4 total.
* **Ativo — Lâmina Tokugawa:** ao matar humanoide, pode entrar em Fúria por 3 turnos; `+2D6 dano`; deve atacar o alvo mais próximo. Determinação CD 16 para sair. Se SAN chegar a 0 durante a Fúria, +1 Corrupção permanente.



### 6.3 Dōjigiri (童子切)

* **Tipo:** Katana / Médio-Larga
* **Dano:** `4D6 + Destreza + Espadas`
* **Custo:** 6 SAN por Decapitação.
* **Passivo — Yokozuna das Espadas:** `+3D6` contra Oni, Demônios, Ogros ou Corrompidos Rank A+.
* **Ativo — Corte do Shuten-dōji:** 1x/combate; se reduzir inimigo Demoníaco a 0 HP, decapita, impede regeneração e aliados a 6m recuperam +5 SAN. Contra humanos: Medo, SAN CD 15.



### 6.4 Jyuzumaru (数珠丸)

* **Tipo:** Katana com Juzu / Médio
* **Dano:** `3D6 + Superno + Selamento`
* **Custo:** 10 SAN por Selamento.
* **Passivo — Alma do Irmão:** contém alma selada ligada à história de Brolly; +4 Concentração para manter selamentos; detecta presenças Superno a 20m.
* **Ativo — Rosário de Purificação:** por 10 SAN e cravada no chão, cria círculo de 4m por 3 turnos; dentro, magias B+ não podem ser conjuradas, mortos-vivos/Yokai não entram e aliados recebem +2 contra possessão.
* **Risco:** uso contínuo pode ameaçar o selo da alma.

### 6.5 Mikazuki-Munechika (三日月宗近)

* **Tipo:** Katana Crescente / Médio
* **Atributo:** Destreza
* **Dano:** `4D6 + Destreza + Espadas`
* **Custo:** 7 SAN por Ilusão.
* **Passivo — Corte da Lua:** +5 Iniciativa quando desembainhada; crítico 19–20 contra desprevenidos.
* **Ativo — Véu de Mikazuki:** 1x/cena; cria 2 ilusões por 2 turnos; ataques contra usuário sofrem Desvantagem; pode trocar de lugar com ilusão como ação livre. Ilusão destruída: Percepção CD 15 ou Cegueira 1 turno.
* **Estado narrativo:** desaparecida no universo Absconditus; localização pertence à campanha.

### 6.6 Onimaru (鬼丸)

* **Tipo:** Katana Guardiã / Médio
* **Atributo:** Reflexo
* **Dano:** `4D6 + Reflexo + Espadas`
* **Custo:** 0 SAN para Guardiã Autônoma.
* **Passivo — Lâmina que se Move Sozinha:** contra ataque surpresa ou usuário dormindo/inconsciente, ataca sozinha com `3D6+5`, sem gastar ação do usuário.
* **Ativo — Pesadelo Cortado:** uma noite ao lado da espada concede +10 SAN extra e imunidade a pesadelos e possessão por 24h. Se emprestada, 50% de chance de retornar ao dono.

### 6.7 Ōtenta (大典太)

* **Tipo:** Katana Larga / Grande; requer Força 3+
* **Atributo:** Força / Superno
* **Dano:** `5D6 + Força + Espadas`
* **Custo:** 8 SAN por Expurgo.
* **Passivo — Barreira Maeda:** aves/insetos não se aproximam a 2m; aliados a 3m recebem +3 HP Máx temporário com a lâmina desembainhada; 1x/dia, toque cura `1D6+2 HP` sem Medicina.
* **Ativo — Expulsão do Corvo:** 8 SAN; pulso de 8m. Yokai, Sombras e Corrompidos fazem Determinação CD 18; falha empurra 6m e impede entrada por 2 turnos. Possuídos fazem CD 20 para expulsão.





\---





## 🧾 7. Implementação e Estado



### Permanentes controlados pela aplicação



* Rank
* Classe
* Raça
* Atributos e pontos manuais
* HP/SAN/Proteção máximos
* Afinidades
* Limite de magias
* Inventário
* Bônus permanentes
* Corrupção



### Decisões do Mestre



* Promoções
* Trocas de magia
* Exceções de equipamento
* Armas encontradas/roubadas
* Consequências narrativas
* Localização de Lendárias
* Eventos sobrenaturais

Trocar Organização oferece novas escolhas e não apaga automaticamente o inventário anterior.





\---





## 🧪 8. Checklist de Auditoria da Ficha



* \[ ] Rank válido.
* \[ ] Classe válida.
* \[ ] Raça válida.
* \[ ] Organização válida.
* \[ ] Atributos entre 0 e 10.
* \[ ] Pontos manuais separados dos bônus.
* \[ ] +2 pontos por promoção aplicado.
* \[ ] HP máximo recalculado.
* \[ ] Proteção recalculada.
* \[ ] SAN máxima recalculada.
* \[ ] Máximo atual não excedido.
* \[ ] Até 3 afinidades.
* \[ ] Até 1/2/3/4/5/5 magias conforme Rank.
* \[ ] Nenhuma magia acima do Rank do personagem.
* \[ ] Custo SAN correto.
* \[ ] Dado correto pelo Rank.
* \[ ] Matriz usa Ar e Raio.
* \[ ] Plasma está presente como evolução de Fogo.
* \[ ] Proteção temporária separada da permanente.
* \[ ] Sangramento limitado a 2D4 e ignorando Proteção.
* \[ ] Equipamento inicial correto.
* \[ ] Lendária não escolhida livremente na criação.





\---





## 📌 9. Resumo Técnico Definitivo



```text


TESTE
1 = Falha Crítica
2–9 = Falha
10–19 = Sucesso Comum
20 = Sucesso Crítico



DANO FÍSICO
Dados da Arma + Atributo + Habilidade



MAGIA
Dados da Magia + Superno



RECURSOS
HP = Rank + Classe + Raça
Proteção = Rank + Classe + Raça
SAN = Rank + Classe + Raça + itens



PROTEÇÃO
Temporária → Permanente → HP
Sangramento ignora Proteção



SANGRAMENTO
1D4/turno, máximo 2D4



MAGIAS CONHECIDAS
E 1 | D 2 | C 3 | B 4 | A 5 | S 6



CUSTOS
E 5 | D 10 | C 15 | B 20 | A 25 | S 35 SAN



DADOS
E 1D6 | D 2D6 | C 3D6 | B 4D6 | A 5D6 | S 6D6



ELEMENTOS


Água → Gelo
Fogo → Plasma
Terra → Metal
Ar → Raio
Luz → Luz Intensificada
Trevas → Trevas Intensificadas



MATRIZ
Vantagem = +1D6
Desvantagem = -1D6
Neutro = 0


```





\---





## 📚 10. Hierarquia de Fontes



1. **REGRAS-CONSOLIDADAS** — limites, implementação, recursos e estados.
2. **Livro de Magias Superno** — sistema místico, elementos, evoluções, magias e matriz.
3. **Armas e Itens** — arsenal, organizações e Lendárias.
4. **Regras e Mecânicas / Conteúdo Mecânico Complementar** — suporte e valores auxiliares.
5. Protótipos, HTMLs e guias rápidos — referência histórica, sem prevalecer sobre as regras atuais.

Quando uma versão antiga contradiz uma regra consolidada, a regra consolidada prevalece. Quando faltar uma regra, a lacuna deve ser registrada para decisão do Game Designer/Mestre, em vez de ser preenchida silenciosamente.





\---





# ✅ 11. Estado Consolidado do Sistema





O núcleo atual de **Absconditus** é composto por:



1. D20 com quatro resultados objetivos.
2. Dano físico baseado em Arma + Atributo + Habilidade.
3. Magia baseada em Dados da Magia + Superno.
4. SAN como recurso de conjuração.
5. HP, Proteção e SAN por Rank + Classe + Raça.
6. Proteção permanente separada de Proteção temporária.
7. Sangramento separado do dano principal e ignorando Proteção.
8. Progressão de magias limitada a 1/2/3/4/5/5.
9. Até três afinidades elementais.
10. Seis Elementos Primários.
11. Seis Evoluções Elementais.
12. Matriz elemental de 12 entradas.
13. Fogo → Plasma.
14. Água → Gelo.
15. Terra → Metal.
16. Ar → Raio.
17. Luz → Luz Intensificada.
18. Trevas → Trevas Intensificadas.
19. Oito Organizações com equipamentos vinculados.
20. Regra especial do Grimório Marcado da Kurotsuki.
21. Sete Armas Superno Lendárias Rank S.
22. Mikazuki-Munechika desaparecida na continuidade do RPG.
23. Aplicação controla estados objetivos; Mestre controla exceções e decisões narrativas.

> \*\*Fim do Documento — Absconditus: Manual Consolidado de Regras do Sistema\*\*
>
> Esta edição deve ser tratada como referência técnica consolidada até nova revisão oficial.







Estrutura da ficha



Resistências

Físico
Espiritual
Magica
Veneno
Elemental


Afinidade Elemental

Os jogadores poderão escolher apenas um elemento, e desenvolver a Evolução Elemental do mesmo de acordo com seu ranking.
Ranking S adquire um segundo elemento e sua Evolução Elemental. Totalizando dois elementos Primários e dois Evolução Elemental.
  
Elementos Primário: ranking E & D & C
Evolução Elemental: ranking B & A
Segundo Elemento Primário e sua Evolução Elemental: ranking S



As magias serão divididas em três categorias:

Dano (Dano causado/dano direto, dano em área)
Suporte (Cura (pessoal, unitária, em área), proteção (pessoal, unitária, em área), bust/buff (pessoal, unitária, em área))
Controle (Controle de área/ Controle de grupo)


Elemento Primário (EP)

Água - 11 magias (Dano 5/Suporte 3/Controle 3)
Fogo - 11 magias (Dano 5/Suporte 3/Controle 3)
Terra - 11 magias (Dano 5/Suporte 3/Controle 3)
Ar - 11 magias (Dano 5/Suporte 3/Controle 3)

Luz - 11 magias (Dano 5/Suporte 3/Controle 3)
Trevas - 11 magias (Dano 5/Suporte 3/Controle 3)


Evolução Elemental (EE)

Água - 11 magias (Dano 5/Suporte 3/Controle 3) -> Evolução elemental -> Gelo - 5 magias - (Dano 3/Suporte 1/Controle 1)
Fogo - 11 magias (Dano 5/Suporte 3/Controle 3) -> Evolução elemental -> Plasma - 5 magias (Dano 3/Suporte 1/Controle 1)
Terra - 11 magias (Dano 5/Suporte 3/Controle 3) -> Evolução elemental -> Metal - 5 magias (Dano 3/Suporte 1/Controle 1)
Ar - 11 magias (Dano 5/Suporte 3/Controle 3) -> Evolução elemental -> Raio - 5 magias (Dano 3/Suporte 1/Controle 1)
Luz - 11 magias (Dano 5/Suporte 3/Controle 3) -> Evolução elemental -> Luz (mantém o elemento mas intensifica o poder) - 5 magias - (Dano 3/Suporte 1/Controle 1)
Trevas - 11 magias (Dano 5/Suporte 3/Controle 3) -> Evolução elemental -> Trevas (mantém o elemento mas intensifica o poder) - 5 magias - (Dano 3/Suporte 1/Controle 1)


Aprendizado de magias por ranking

Ranking E - 1 magia -> Elemento Primário 
Ranking D - 2 magias -> Elemento Primário
Ranking C - 2 magias -> Elemento Primário
Ranking B - 2 magias -> Elemento Primário + 2 magias -> Evolução Elemental 
Ranking A - 3 magias -> Elemento Primário + 2 magias -> Evolução Elemental  
Ranking S - 1 magia -> Elemento Primário + 1 magia -> Evolução Elemental 



Slot de magias desbloqueados por ranking:

E - 1 Slot de magia
D - 2 Slots de magias
C - 3 Slots de magias
B - 4 Slots de magias
A - 5 Slots de magias
S - 6 Slots de magias


Cada ranking aumenta o (Dano/Suporte/Controle) da magia 
quanto maior o ranking, melhor é a magia 





