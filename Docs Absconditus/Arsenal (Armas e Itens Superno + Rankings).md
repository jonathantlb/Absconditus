# ABSConditus --- Arsenal (Armas e Itens)

**Documento normativo --- versão consolidada**\
**Sistema de Ranking e Cores de Equipamentos**

Este documento reúne as regras de armas, itens convencionais, itens
Superno, consumíveis, vínculos organizacionais e armas Superno
lendárias. Também formaliza o sistema de rankings E--S e suas cores, que
passa a ser o padrão de classificação do Arsenal.

> **Princípio central:** o ranking representa o valor geral de um
> equipamento em termos de poder, utilidade, versatilidade, efeitos
> especiais e excepcionalidade. Ranking não é sinônimo exclusivo de
> dano.

------------------------------------------------------------------------

## 1. Sistema oficial de Ranking

Todo equipamento catalogado no Arsenal deve possuir um ranking. A
classificação vai de E a S, sendo E a categoria mais comum e S a
categoria excepcional.

  --------------------------------------------------------------------------------
  Ranking        Categoria      Cor oficial    Código HEX     Diretriz geral
  -------------- -------------- -------------- -------------- --------------------
  **E**          Comum          Branco         `#FFFFFF`      Equipamentos
                                                              básicos, acessíveis
                                                              e sem efeitos
                                                              extraordinários.

  **D**          Incomum        Verde          `#22C55E`      Equipamentos
                                                              confiáveis, com
                                                              desempenho ou
                                                              utilidade
                                                              específicos.

  **C**          Raro           Azul           `#3B82F6`      Equipamentos
                                                              especializados, com
                                                              vantagens táticas
                                                              relevantes.

  **B**          Muito raro     Roxo           `#A855F7`      Equipamentos
                                                              poderosos, capazes
                                                              de influenciar
                                                              significativamente
                                                              uma situação ou
                                                              combate.

  **A**          Épico          Laranja        `#F97316`      Equipamentos
                                                              excepcionais, de
                                                              grande poder e
                                                              difícil obtenção.

  **S**          Lendário       Vermelho       `#EF4444`      Relíquias
                                                              extraordinárias,
                                                              únicas ou de
                                                              importância
                                                              sobrenatural,
                                                              histórica ou
                                                              narrativa.
  --------------------------------------------------------------------------------

### 1.1. Critérios de avaliação

A classificação deve considerar o conjunto das características do
equipamento, e não apenas seu dano.

1.  **Dano:** potencial ofensivo e capacidade de causar dano ou
    neutralizar alvos.
2.  **Utilidade:** benefícios que não dependem de causar dano direto,
    como cura, proteção, recuperação ou investigação.
3.  **Versatilidade:** quantidade e variedade de situações em que o
    equipamento pode ser útil.
4.  **Efeitos especiais:** habilidades exclusivas, controle de campo,
    bônus, efeitos sobrenaturais e alterações de regras.
5.  **Limitações:** custo de SAN, consumo de recursos, condições de
    ativação, penalidades, riscos e restrições.

As limitações devem ser consideradas no balanceamento, mas não aumentam
automaticamente o ranking. Uma maldição ou um risco narrativo, por si
só, não torna um item mais poderoso.

### 1.2. Diretrizes por categoria

-   **Rank E --- Comum:** equipamento básico, com efeito simples, baixo
    impacto ou utilidade limitada.
-   **Rank D --- Incomum:** equipamento convencional e confiável, com
    desempenho consistente ou benefício específico.
-   **Rank C --- Raro:** equipamento especializado que oferece vantagem
    tática relevante ou utilidade diferenciada.
-   **Rank B --- Muito raro:** equipamento com dano elevado, habilidade
    relevante ou capacidade de mudar o curso de um combate ou situação.
-   **Rank A --- Épico:** equipamento excepcional, com desempenho
    extraordinário e vantagem decisiva em determinadas circunstâncias.
-   **Rank S --- Lendário:** relíquia de poder extraordinário, com
    habilidades únicas e relevância histórica, mística ou narrativa.

### 1.3. Regras gerais do ranking

1.  **Ranking não é nível de personagem.** Um personagem pode utilizar
    equipamentos de diferentes rankings, desde que cumpra seus
    requisitos e regras.
2.  **Ranking de equipamento não é ranking de magia.** Um item Rank B
    pode auxiliar uma magia de Rank E ou S; são classificações
    independentes.
3.  **Equipamentos do mesmo ranking não precisam ter funções ou poder
    idênticos.** O ranking expressa uma faixa geral de excepcionalidade,
    não equivalência matemática.
4.  **O ranking não substitui os atributos, requisitos, custos ou regras
    próprias do item.**
5.  **Penalidades e maldições não elevam automaticamente o ranking.** A
    avaliação considera o poder efetivo do equipamento e suas
    limitações.
6.  **O ranking deve ser revisto quando o efeito de um item for
    alterado.** Uma mudança relevante de dano, alcance, custo,
    frequência ou habilidade especial pode justificar reclassificação.
7.  **Rank S é excepcional.** A categoria deve ser reservada a relíquias
    extraordinárias. No catálogo atual, as sete Armas Superno Lendárias
    são Rank S.

### 1.4. Uso das cores

As cores devem ser aplicadas de maneira consistente em fichas,
inventários, bibliotecas, grimórios, listas de equipamentos, cartões de
item e demais interfaces do sistema.

-   O texto do ranking deve permanecer legível sobre fundos claros e
    escuros.
-   A cor identifica a categoria; não substitui a indicação escrita do
    ranking.
-   Em interfaces sem suporte a cores, a identificação textual (E, D, C,
    B, A ou S) continua obrigatória.

------------------------------------------------------------------------

## 2. Atributos e regras gerais de armas

Os atributos seguem estas diretrizes:

-   Armas de longo alcance usam **Precisão**.
-   Espadas e lâminas usam **Destreza**.
-   **Força** cobre mover, empurrar, carregar e golpear.
-   **Agilidade** determina iniciativa e movimentação.

### 2.1. Fórmula de dano

`Dano = dados da arma + Atributo + Habilidade relevante`

Exemplo: uma arma de 2D6 com Destreza 4 e Habilidade 4 causa
`2D6 + 4 + 4`.

### 2.2. Regra de Sangramento

No crítico 20, armas que possuam essa propriedade aplicam **1D4 de dano
por turno** até o alvo ser curado.

-   O acúmulo máximo é 2x (2D4 por turno).
-   Um teste de Medicina CD 12 encerra o sangramento.
-   Um Kit Médico + Medicina CD 10 também encerra o sangramento.
-   Bastões não causam sangramento.

Quando uma arma possuir uma regra especial de sangramento própria, essa
regra específica prevalece.

### 2.3. Regra recomendada de HP e SAN

-   **HP Máx = 10 + (Força x 2) + (Resistências x 1).**
-   **SAN Máx = 30 + (Inteligência x 2) + (Determinação x 2).**

Esta fórmula é uma recomendação de balanceamento para manter a
letalidade Noir sem garantir eliminações em um único golpe.

------------------------------------------------------------------------

## 3. Armas brancas

  ------------------------------------------------------------------------------------
  Arma               Porte                 Dano Atributo    Regra          Ranking
  ------------------ ----------- -------------- ----------- -------------- -----------
  Faca               Leve                   1D6 Destreza    Sangramento no **E ---
                                                            crítico 20     Branco**

  Estrelas ninja     Leve                   1D6 Destreza    Sangramento no **E ---
                                                            crítico 20;    Branco**
                                                            arremesso usa  
                                                            Precisão       

  Bastão curto       Médio                1D6+1 Força       Contundente;   **E ---
                                                            sem            Branco**
                                                            sangramento;   
                                                            causa          
                                                            Atordoamento   
                                                            se dano \>     
                                                            Força do alvo  

  Katana             Média                  2D6 Destreza    Sangramento no **D ---
                                                            crítico 20     Verde**

  Espada reta        Média                  2D6 Destreza    Sangramento no **D ---
                                                            crítico 20     Verde**

  Adaga              Leve                 1D6+1 Destreza    Sangramento no **D ---
                                                            crítico 20     Verde**

  Bastão longo       Grande                 2D6 Força       Contundente;   **D ---
                                                            sem            Verde**
                                                            sangramento;   
                                                            causa          
                                                            Atordoamento   

  Corrente/Chicote   Médio                1D6+1 Destreza    Controle; pode **D ---
                                                            desarmar       Verde**
                                                            conforme       
                                                            decisão do     
                                                            mestre         

  Arco & Flecha      Médio                  2D6 Precisão    Sangramento no **D ---
                                                            crítico 20;    Verde**
                                                            longo alcance  

  Rapieira           Média                  2D6 Destreza    Sangramento no **C ---
                                                            crítico 20;    Azul**
                                                            favorece       
                                                            estocadas;     
                                                            crítico 19--20 
                                                            se alvo        
                                                            desprevenido   

  Machado 1 mão      Grande               2D6+1 Força       Sangramento no **C ---
                                                            crítico 20     Azul**

  Machado 2 mãos     Muito                  3D6 Força       Sangramento no **B ---
                     grande                                 crítico 20;    Roxo**
                                                            requer duas    
                                                            mãos; -2       
                                                            Agilidade na   
                                                            iniciativa     
  ------------------------------------------------------------------------------------

### 3.1. Justificativa da classificação

-   **Rank E:** faca, estrelas ninja e bastão curto são opções simples,
    com dano ou aplicação mais limitados.
-   **Rank D:** katana, espada reta, adaga, bastão longo,
    corrente/chicote e arco são armas convencionais e eficientes, sem
    efeitos extraordinários no conjunto atual de regras.
-   **Rank C:** rapieira possui uma condição especial de crítico;
    machado de uma mão oferece dano superior ao das armas médias.
-   **Rank B:** machado de duas mãos apresenta dano base elevado (3D6),
    compensado pela exigência de duas mãos e pela penalidade de
    iniciativa.

------------------------------------------------------------------------

## 4. Armas de fogo

  -------------------------------------------------------------------------
  Arma                       Dano Atributo      Observação    Ranking
  ------------- ----------------- ------------- ------------- -------------
  Pistola                     2D6 Precisão      Compacta;     **E ---
                                                sangramento   Branco**
                                                no crítico 20 

  SMG                       2D6+1 Precisão      Curto/médio   **C ---
                                                alcance;      Azul**
                                                sangramento   
                                                no crítico    
                                                20; pode      
                                                gastar 3      
                                                balas para    
                                                rolar com     
                                                Vantagem      
                                                1x/turno      

  Rifle de                  3D6+2 Precisão      Médio/longo   **B ---
  assalto                                       alcance;      Roxo**
                                                sangramento   
                                                no crítico 20 

  Rifle de                  4D6+3 Precisão      Longo         **A ---
  precisão                                      alcance;      Laranja**
                                                sangramento   
                                                no crítico    
                                                20; requer 1  
                                                ação para     
                                                mirar (ganha  
                                                +2 Precisão   
                                                no disparo)   
  -------------------------------------------------------------------------

No crítico 20, armas de fogo aplicam **1D4 de Sangramento por turno**
até o alvo ser curado. Máximo de 2D4.

### 4.1. Justificativa da classificação

-   **Pistola --- E:** armamento básico, compacto e de uso geral.
-   **SMG --- C:** oferece uma opção tática de Vantagem mediante gasto
    de munição.
-   **Rifle de assalto --- B:** dano elevado de 3D6+2 e aplicação em
    médio/longo alcance.
-   **Rifle de precisão --- A:** maior dano base entre as armas
    convencionais listadas (4D6+3), com bônus de Precisão ao mirar.

------------------------------------------------------------------------

## 5. Granadas

  ------------------------------------------------------------------------
  Item                              Raio Dano/Efeito      Ranking
  ---------------- --------------------- ---------------- ----------------
  Granada de Luz                     5 m Sem dano; alvos  **C --- Azul**
                                         na área fazem    
                                         teste Percepção  
                                         CD 13; falha     
                                         causa cegueira   
                                         por 1 turno + -2 
                                         Precisão por 2   
                                         turnos           

  Granada de                         6 m Sem dano; cria   **C --- Azul**
  Fumaça                                 cobertura pesada 
                                         por 3 turnos;    
                                         quem atacar      
                                         através da área  
                                         tem Desvantagem; 
                                         quem entrar      
                                         precisa teste    
                                         Percepção CD 12  

  Granada de                         4 m 3D6 de dano;     **B --- Roxo**
  Fragmentação                           aplica dano a    
                                         todos na área;   
                                         aliados fazem    
                                         teste Agilidade  
                                         CD 14 para meio  
                                         dano             
  ------------------------------------------------------------------------

Estas granadas são equipamentos de área e não usam o custo de SAN.

### 5.1. Justificativa da classificação

-   **Luz e Fumaça --- C:** oferecem controle de campo e vantagens
    táticas relevantes, mesmo sem dano direto.
-   **Fragmentação --- B:** causa 3D6 de dano em área e pode atingir
    vários alvos simultaneamente.

------------------------------------------------------------------------

## 6. Itens Superno

Itens Superno usam **Superno e SAN** como eixo de uso.

  ---------------------------------------------------------------------------------
  Item              Efeito passivo         Regra de uso           Ranking
  ----------------- ---------------------- ---------------------- -----------------
  Amuleto           +5 SAN máximo          Não recupera SAN por   **E --- Branco**
                                           si só                  

  Grimório/Tomo     +2 Superno em testes   Não reduz custo de SAN **D --- Verde**
                    de                                            
                    conjuração/ocultismo                          
                    feitos através dele                           

  Varinha           +1D6 no efeito de uma  O D6 adicional é       **B --- Roxo**
                    magia por cena         aplicado antes de      
                                           vantagem/desvantagem   
                                           elemental              

  Cajado            +3 Superno para uma    Não altera o custo de  **B --- Roxo**
                    magia de cura/proteção SAN                    
                    por cena                                      

  Anel              1 vez por cena,        Custo de SAN é pago    **B --- Roxo**
                    permite repetir a      apenas uma vez         
                    rolagem de efeito de                          
                    uma magia, mantendo o                         
                    segundo resultado                             
  ---------------------------------------------------------------------------------

### 6.1. Limite dos bônus

Bônus de itens não mudam o atributo Superno permanente, salvo o bônus
explicitamente indicado pelo item. Eles afetam a resolução da magia
conforme sua descrição.

### 6.2. Justificativa da classificação

-   **Amuleto --- E:** oferece um bônus passivo limitado de SAN máximo.
-   **Grimório/Tomo --- D:** melhora testes de conjuração e ocultismo,
    mas não reduz o custo de SAN.
-   **Varinha --- B:** acrescenta 1D6 ao efeito de uma magia por cena.
-   **Cajado --- B:** concede +3 Superno a uma magia de cura ou proteção
    por cena.
-   **Anel --- B:** permite repetir uma rolagem de efeito mágico,
    mantendo o segundo resultado, com custo de SAN pago apenas uma vez.

### 6.3. Grimório Marcado da Kurotsuki

O Grimório inicial da Kurotsuki é roubado e marcado.

-   **Ranking:** D --- Verde.
-   **Bônus:** concede +2 Superno normalmente.
-   **Risco:** toda vez que o portador usar magia de Ranking B ou
    superior através dele, role 1D6. Em resultado 1, um Coletor da
    Kurotsuki ou entidade rastreadora sente a localização do Grimório.
-   **Classificação:** é uma variante do Grimório/Tomo, não uma
    categoria de ranking independente.

O risco de rastreamento cria um gancho investigativo Noir, mas não eleva
o ranking do item. Seu equilíbrio em relação às demais facções decorre
de ser um vínculo híbrido Físico + Mágico.

------------------------------------------------------------------------

## 7. Consumíveis e equipamentos médicos

  -----------------------------------------------------------------------
  Item              Efeito            Regra             Ranking
  ----------------- ----------------- ----------------- -----------------
  Erva do Véu       Recupera +20 SAN  Sujeita às regras **C --- Azul**
                                      de tolerância     
                                      abaixo            

  Kit Médico        Recupera +20 HP   Exige Habilidade  **D --- Verde**
                                      de Medicina para  
                                      uso               
  -----------------------------------------------------------------------

### 7.1. Erva do Véu

**Nome temático:** *Erva do Véu*.

-   **Uso:** recupera +20 SAN.
-   **Limite:** recuperação não pode ultrapassar a SAN total da ficha.
-   **Tolerância na mesma cena:** após o personagem consumir 2 Ervas do
    Véu na mesma cena, cada erva adicional consumida naquela cena
    recupera apenas +5 SAN.
-   **Uso contínuo:** se consumir ervas em 3 cenas consecutivas, a
    próxima erva recupera apenas +5 SAN.
-   **Recuperação da tolerância:** após uma cena completa sem consumir
    erva, a tolerância volta ao normal.
-   **Risco:** em falha crítica (1 no D20) ao usar Erva com tolerância
    ativa, role na Tabela de Corrupção Leve.
-   **Limite narrativo:** a erva não substitui sono como método natural
    de recuperação.

### 7.2. Kit Médico

-   Recupera +20 HP.
-   Exige Habilidade de Medicina para uso.
-   Também pode ser utilizado para encerrar Sangramento conforme as
    regras gerais, com Medicina CD 10.

### 7.3. Justificativa da classificação

-   **Kit Médico --- D:** recuperação relevante, condicionada à
    Habilidade de Medicina.
-   **Erva do Véu --- C:** recupera SAN, recurso essencial para usuários
    de poderes Superno, mas possui tolerância e risco de Corrupção.

------------------------------------------------------------------------

## 8. Vínculo de armas por Organização

Ao escolher uma organização, o personagem recebe **duas armas padrão, 2
kits médicos e 2 Ervas do Véu**. Além disso, pode substituir **uma das
duas armas** por uma única arma pertencente a outra organização.

  -----------------------------------------------------------------------
  Organização             Conceito                Armas padrão
  ----------------------- ----------------------- -----------------------
  Credo do Caçador        Combate / eliminar      Machado 1 mão + Pistola
                          ameaças                 

  Centro de Observação    Investigação /          Pistola + Faca
                          compreender e registrar 

  Pax Vobiscum            Religião / proteger e   Grimório/Tomo + Amuleto
                          purificar               

  Filhos da Terra         Natureza / preservar    Varinha + Cajado
                          equilíbrio              

  Ordem do Abismo         Magia sombria /         Grimório/Tomo + Adaga
                          explorar o proibido     

  A Divisão               Atiradores / conter     Rifle de assalto +
                          danos à sociedade       Pistola

  Clã Akamatsu 赤松氏     Espadachins /           Katana + Arco & Flecha
                          disciplina e domínio    
                          das lâminas             

  Kurotsuki 黒月          Roubo / Contrabando /   Katana + Grimório/Tomo
                          Comércio ilegal de      Marcado
                          objetos Superno         
  -----------------------------------------------------------------------

**Observação:** itens Superno contam como uma das duas
armas/equipamentos padrão para fins de vínculo; o personagem ainda
recebe os 2 kits médicos e 2 Ervas do Véu.

### 8.1. Kurotsuki 黒月 --- Lua Negra

Uma pequena organização japonesa especializada em roubo, contrabando e
comércio ilegal de objetos Superno.

Atua principalmente no mercado clandestino de antiguidades, armas
históricas e relíquias mágicas.

-   **Conceito:** roubo / contrabando / comércio ilegal de objetos
    Superno.
-   **Armas:** Katana + Grimório/Tomo Marcado.

**Regra de Substituição:** o jogador pode trocar uma das duas armas
padrão por qualquer outra de outra organização. Não pode escolher Arma
Superno Lendária na criação.

------------------------------------------------------------------------

## 9. Armas Superno Lendárias --- Ranking S

Todas as armas desta seção são **Rank S --- Vermelho**.

### 9.1. Requisitos gerais

-   Superno 5.
-   5 pontos na Habilidade da arma.
-   SAN Máx 40+.
-   Causam 1 Corrupção se usadas com SAN \< 10.
-   No crítico 20, aplicam 2D4 Sangramento + Efeito Especial.

### 9.2. Tentetsutou (天鉄刀) --- Rank S

-   **Tipo / Porte:** Katana / Médio.
-   **Rolagem de Dano Base:** 4D6 + Superno + Espadas.
-   **Custo de SAN Ativo:** 0 SAN passivo / 8 SAN para Sobrecarga de
    Meteorito.
-   **Efeito Passivo / Habilidade Especial:** Condutor de Superno.
    -   **Passivo:** ignora 2 pontos de Resistência Espiritual do alvo
        em todo dano Superno canalizado pela lâmina.
    -   **Ativo:** Chuva de Ferro (1x/cena) --- ao gastar 8 SAN,
        converte todo dano da arma em dano Superno puro por 2 turnos e
        adiciona Superno novamente ao dano. Após uso, -2 Percepção por 1
        cena.
-   **História:** lâmina forjada de meteorito por Yoshindo Yoshihara, em
    posse de Vicky.

### 9.3. Muramasa (村正) --- Rank S

-   **Tipo / Porte:** Katana Amaldiçoada / Médio.
-   **Rolagem de Dano Base:** 5D6 + Destreza + Espadas.
-   **Custo de SAN Ativo:** 5 SAN por turno em Fúria.
-   **Efeito Passivo / Habilidade Especial:** Sede Incessante.
    -   **Passivo:** causa Sangramento 1D4 automático em acerto (sem
        precisar de crítico). No crítico 20, Sangramento 2D4.
    -   **Ativo:** Lâmina Tokugawa --- ao matar humanoide, pode entrar
        em Fúria: +2D6 dano por 3 turnos, mas deve atacar o alvo mais
        próximo (amigo ou inimigo) a cada turno. Teste Determinação CD
        16 para sair. Se SAN chegar a 0 em Fúria, ganha 1 Corrupção
        permanente.
-   **História:** conhecida como Katana Maldita, responsável por mortes
    da família Tokugawa.

### 9.4. Tenka-Göken 天下五剣

Tenka-Göken (天下五剣), "Cinco Espadas Sob os Céus", é o nome de um
grupo de cinco espadas Katana Superno lendárias do período Muromachi.

#### 9.4.1. Dōjigiri (童子切) --- Rank S

-   **Tipo / Porte:** Katana / Médio --- Larga.
-   **Rolagem de Dano Base:** 4D6 + Destreza + Espadas.
-   **Custo de SAN Ativo:** 6 SAN por Decapitação.
-   **Efeito Passivo / Habilidade Especial:** Yokozuna das Espadas.
    -   **Passivo:** Matadora de Oni --- +3D6 dano contra criaturas Oni,
        Demônio, Ogro ou Corrompido Rank A+.
    -   **Ativo:** Corte do Shuten-dōji (1x/combate) --- declare antes
        de rolar. Se reduzir inimigo Demoníaco a 0 HP, decapita
        automaticamente, impede regeneração e aliados em 6m recuperam +5
        SAN. Contra humanos causa Medo (teste SAN CD 15).
-   **História:** Minamoto no Yorimitsu matou o ogro Shuten-dōji com
    ela. Mantida no Museu Nacional de Tóquio.

#### 9.4.2. Jyuzumaru (数珠丸) --- Rank S

-   **Tipo / Porte:** Katana com Juzu / Médio.
-   **Rolagem de Dano Base:** 3D6 + Superno + Selamento.
-   **Custo de SAN Ativo:** 10 SAN por Selamento.
-   **Efeito Passivo / Habilidade Especial:** Rosário Budista.
    -   **Passivo:** Alma do Irmão de Brolly --- contém alma selada. +4
        Concentração para manter selamentos e sente presenças Superno a
        20m.
    -   **Ativo:** Rosário de Purificação --- ao gastar 10 SAN e cravar
        no chão, cria círculo de 4m por 3 turnos. Dentro, nenhuma magia
        Rank B+ pode ser conjurada, mortos-vivos e Yokai não entram,
        aliados ganham +2 contra possessão.
    -   **Risco narrativo:** uso contínuo pode libertar a alma selada.
-   **História:** nome vem do rosário budista que adornava a espada.
    Exposta 3 de novembro no Honko-ji, Hyogo.

#### 9.4.3. Mikazuki-Munechika (三日月宗近) --- Rank S

-   **Tipo / Porte:** Katana Crescente / Médio --- Curva Perfeita.
-   **Rolagem de Dano Base:** 4D6 + Destreza + Espadas.
-   **Custo de SAN Ativo:** 7 SAN por Ilusão.
-   **Efeito Passivo / Habilidade Especial:** Lua Crescente.
    -   **Passivo:** Corte da Lua --- +5 iniciativa quando
        desembainhada. Crítico 19--20 contra alvos desprevenidos.
    -   **Ativo:** Véu de Mikazuki (1x/cena) --- cria 2 ilusões por 2
        turnos. Ataques contra usuário têm Desvantagem. Pode trocar de
        lugar com ilusão como ação livre. Ilusão destruída causa teste
        Percepção CD 15 ou Cegueira 1 turno pela luz lunar.
-   **História:** mais antiga remanescente do século X, guardada no
    Museu Nacional de Tóquio. Elegante e voltada a ocultamento.

#### 9.4.4. Onimaru (鬼丸) --- Rank S

-   **Tipo / Porte:** Katana Guardiã / Médio.
-   **Rolagem de Dano Base:** 4D6 + Reflexo + Espadas.
-   **Custo de SAN Ativo:** 0 SAN (Guardiã Autônoma).
-   **Efeito Passivo / Habilidade Especial:** Lâmina que se Move
    Sozinha.
    -   **Passivo:** quando usuário é atacado de surpresa ou está
        Dormindo/Inconsciente, Onimaru ataca sozinha com 3D6+5 contra
        agressor. Não gasta ação.
    -   **Ativo:** Pesadelo Cortado --- passar noite com Onimaru ao lado
        recupera +10 SAN extra e imunidade a pesadelos e possessão por
        24h. Se emprestada, 50% de chance de voltar sozinha ao dono.
-   **História:** lenda diz que Hōjō Tokiyori limpou a espada manchada e
    ela cortou sozinha o pescoço de um Oni de prata que causava
    pesadelos. Mantida pela Agência Casa Imperial.

#### 9.4.5. Ōtenta (大典太) --- Rank S

-   **Tipo / Porte:** Katana Larga (3,5 cm) / Grande --- Requer Força
    3+.
-   **Rolagem de Dano Base:** 5D6 + Força + Espadas.
-   **Custo de SAN Ativo:** 8 SAN por Expurgo.
-   **Efeito Passivo / Habilidade Especial:** Barreira Maeda.
    -   **Passivo:** largura anormal repele sobrenatural.
        Pássaros/insetos não se aproximam a 2m. Aliados a 3m ganham +3
        HP Máx temporário com lâmina desembainhada. 1x/dia, tocar lâmina
        em aliado cura 1D6+2 HP sem Medicina.
    -   **Ativo:** Expulsão do Corvo --- ao gastar 8 SAN e erguer
        lâmina, pulso 8m. Yokai, Sombras e Corrompidos fazem teste
        Determinação CD 18 ou são empurrados 6m e não podem entrar por 2
        turnos. Contra possuídos, chance de expulsar entidade CD 20.
-   **História:** lenda diz que curou a filha de Maeda Toshiie e que
    nenhuma ave se aproxima de onde está armazenada. Regalia dos shoguns
    Ashikaga. Mantida por Maeda-ikueikai.

### 9.5. Regra Geral Rank S

Todas as 7 Lendárias ignoram imunidade a Sangramento de criaturas Rank
A-. Se o usuário falhar em teste de SAN enquanto empunha Rank S, role
1D6: em 1, a arma toma controle por 1 turno, narrado pelo mestre.

------------------------------------------------------------------------

## 10. Resumo oficial da distribuição

A contagem abaixo considera cada modelo-base uma vez. O Grimório Marcado
é uma variante do Grimório/Tomo e não é contado como um modelo
independente.

  ---------------------------------------------------------------------------
  Ranking          Cor                         Quantidade Equipamentos
  ---------------- ---------------- --------------------- -------------------
  **E**            Branco                           **5** Faca, Estrelas
                                                          ninja, Bastão
                                                          curto, Pistola,
                                                          Amuleto

  **D**            Verde                            **8** Katana, Espada
                                                          reta, Adaga, Bastão
                                                          longo,
                                                          Corrente/Chicote,
                                                          Arco & Flecha,
                                                          Grimório/Tomo, Kit
                                                          Médico

  **C**            Azul                             **6** Rapieira, Machado 1
                                                          mão, SMG, Granada
                                                          de Luz, Granada de
                                                          Fumaça, Erva do Véu

  **B**            Roxo                             **6** Machado 2 mãos,
                                                          Rifle de assalto,
                                                          Granada de
                                                          Fragmentação,
                                                          Varinha, Cajado,
                                                          Anel

  **A**            Laranja                          **1** Rifle de precisão

  **S**            Vermelho                         **7** As sete Armas
                                                          Superno Lendárias

  **Total**        ---                             **33** 33 modelos-base
  ---------------------------------------------------------------------------

### 10.1. Distribuição visual

-   **E --- Branco:** equipamentos comuns.
-   **D --- Verde:** equipamentos convencionais e confiáveis.
-   **C --- Azul:** equipamentos especializados.
-   **B --- Roxo:** equipamentos muito poderosos.
-   **A --- Laranja:** equipamentos excepcionais.
-   **S --- Vermelho:** relíquias lendárias.

------------------------------------------------------------------------

## 11. Diretrizes para futuras inclusões no Arsenal

Toda nova arma ou item adicionado ao documento deve apresentar, no
mínimo:

1.  **Nome do equipamento.**
2.  **Categoria:** arma branca, arma de fogo, granada, item Superno,
    consumível ou outra categoria pertinente.
3.  **Ranking e cor.**
4.  **Dano ou efeito.**
5.  **Atributo utilizado**, quando aplicável.
6.  **Alcance, porte ou área**, quando aplicável.
7.  **Custo e condições de uso**, quando aplicáveis.
8.  **Limitações, riscos e efeitos colaterais**, quando aplicáveis.

### 11.1. Processo de classificação

Para classificar um novo equipamento:

1.  Descrever seu funcionamento completo, sem definir o ranking
    antecipadamente.
2.  Avaliar dano, utilidade, versatilidade e efeitos especiais.
3.  Identificar custos, restrições e riscos.
4.  Comparar o equipamento com os itens já classificados no Arsenal.
5.  Atribuir o ranking que melhor representa seu impacto geral.
6.  Registrar a cor correspondente.
7.  Revisar a classificação após testes de jogo, se o equipamento
    demonstrar desempenho muito acima ou abaixo do esperado.

### 11.2. Regra de consistência

Equipamentos com efeitos equivalentes devem receber classificações
semelhantes, salvo quando houver diferenças relevantes de custo,
frequência, alcance, requisitos, risco ou versatilidade.

A classificação não deve ser elevada apenas para tornar um item
aparentemente mais raro, nem reduzida apenas porque seu efeito não causa
dano.

### 11.3. Alterações futuras

Qualquer alteração no dano, nos efeitos, no custo de SAN, na frequência
de uso ou nos requisitos de um equipamento deve ser registrada no
Arsenal. Se a alteração modificar significativamente seu poder geral, o
ranking deve ser reavaliado.

------------------------------------------------------------------------

**ABSConditus --- Arsenal (Armas e Itens)**\
*Documento de referência para classificação, consulta e padronização dos
equipamentos do sistema.*
