dropTagno="drop table if exists agno cascade"
dropTregion="drop table if exists region cascade"
dropTcomuna="drop table if exists comuna cascade"
dropTdeptoProv="drop table if exists deptoProv cascade"
dropTrural="drop table if exists rural cascade"
dropTestadoEstab ="drop table if exists estadoEstab cascade"
dropTdependencia ="drop table if exists dependencia cascade"
dropTprovincia ="drop table if exists provincia cascade"
dropTestablecimiento="drop table if exists establecimiento cascade"

dropTense ="drop table if exists ense cascade"
dropTense2 ="drop table if exists ense2 cascade"
dropTgrado ="drop table if exists grado cascade"
dropTjornada ="drop table if exists jornada cascade"
dropTtipoCurso ="drop table if exists tipoCurso cascade"
dropTdescrCurso ="drop table if exists descrCurso cascade"
dropTcurso ="drop table if exists curso cascade"

dropTgeneroAl ="drop table if exists generoAl cascade"
dropTintegradoAl ="drop table if exists integradoAl cascade"
dropTdiferencialAl ="drop table if exists diferencialAl cascade"
dropTalumno ="drop table if exists alumno cascade"

dropTrama ="drop table if exists rama cascade"
dropTsector ="drop table if exists sector cascade"
dropTespecialidad ="drop table if exists especialidad cascade"
dropTsituacion ="drop table if exists situacion cascade"
dropTsituacionR ="drop table if exists situacionR cascade"
dropTmencion ="drop table if exists mencion cascade"
dropTfact_rendimiento ="drop table if exists fact_rendimiento cascade"


createTagno ='''CREATE TABLE agno(
agno int primary key
)'''


createTregion ='''CREATE TABLE region(
cod_reg int primary key,
nom_reg varchar
)'''

createTprovincia ='''CREATE TABLE provincia(
cod_pro_rbd int primary key,
nom_pro_rbd varchar
)'''

createTcomuna ='''CREATE TABLE comuna(
cod_com int primary key,
nom_com varchar
)'''


createTdeptoProv ='''CREATE TABLE deptoProv(
cod_deprov_rbd int primary key,
nom_deprov_rbd varchar
)'''


createTestadoEstab ='''CREATE TABLE estadoEstab(
estado_estab int primary key,
nom_estado_estab varchar
)'''

createTdependencia ='''CREATE TABLE dependencia( --
cod_depe int primary key,
nom_depe varchar
)'''

createTrural ='''CREATE TABLE rural( --
cod_rural int primary key,
nom_rural varchar
)'''

createTestablecimiento ='''CREATE TABLE establecimiento(
rbd int primary key, --cod_com no esta
dgv_rbd int,
nom_rbd varchar,
cod_pro_rbd int,
rural_rbd int,
estado_estab int,
cod_depe int,


cod_reg_rbd int,
cod_com_rbd int,
cod_deprov_rbd int,

foreign key (cod_reg_rbd) references region(cod_reg),
foreign key (cod_deprov_rbd) references deptoProv(cod_deprov_rbd),
foreign key (estado_estab) references estadoEstab(estado_estab),
foreign key (cod_depe) references dependencia(cod_depe),
foreign key (cod_pro_rbd) references provincia(cod_pro_rbd),
foreign key (rural_rbd) references rural(cod_rural),
foreign key (cod_com_rbd) references comuna(cod_com)

)'''

createTense ='''CREATE TABLE ense(
cod_ense int primary key,
nom_ense varchar
)'''

createTense2 ='''CREATE TABLE ense2(
cod_ense2 int primary key,
nom_ense2 varchar
)'''

createTgrado ='''CREATE TABLE grado(
cod_grado int,
cod_ense int,
nom_grado varchar,

primary key(cod_grado,cod_ense),
foreign key (cod_ense) references ense(cod_ense)

)'''

createTjornada ='''CREATE TABLE jornada(
cod_jor int primary key,
nom_jor varchar
)'''

createTtipoCurso ='''CREATE TABLE tipoCurso(
cod_tip_cur int primary key,
nom_tip_cur varchar
)'''

createTdescrCurso ='''CREATE TABLE descrCurso(
cod_des_cur int primary key,
nom_des_cur varchar
)'''

createTcurso ='''CREATE TABLE curso(
cod_curso int primary key, --codigo generado por nosotros
cod_ense int, --traducido
cod_ense2 int, --traducido
cod_grado int, --traducido
let_cur varchar, 
cod_jor int, --traducido
cod_tip_cur int, --traducido
cod_des_cur int, --traducido

foreign key (cod_ense2) references ense2(cod_ense2),
foreign key (cod_grado,cod_ense) references grado(cod_grado,cod_ense),
foreign key (cod_jor) references jornada(cod_jor),
foreign key (cod_tip_cur) references tipoCurso(cod_tip_cur),
foreign key (cod_des_cur) references descrCurso(cod_des_cur)

)'''

createTgeneroAl ='''CREATE TABLE generoAl(
gen_alu int primary key,
nom_gen_alu varchar
)'''

createTintegradoAl ='''CREATE TABLE integradoAl(
int_alu int primary key,
nom_gen_alu varchar
)'''

createTdiferencialAl ='''CREATE TABLE diferencialAl(
gd_alu int primary key,
nom_gen_alu varchar
)'''

createTalumno ='''CREATE TABLE alumno(
mrun int primary key,
gen_alu int, --se puede traducir
fec_nac_alu int, 

int_alu int,
gd_alu int, 

foreign key (gen_alu) references generoAl(gen_alu),
foreign key (int_alu) references integradoAl(int_alu),
foreign key (gd_alu) references diferencialAl(gd_alu)

)'''

createTrama ='''CREATE TABLE rama(
cod_rama int primary key,
nom_rama varchar
)'''

createTsector ='''CREATE TABLE sector(
cod_sec int primary key,
nom_sec varchar
)'''

createTespecialidad ='''CREATE TABLE especialidad(
cod_espe int primary key,
nom_espe varchar
)'''

createTsituacion ='''CREATE TABLE situacion(
sit_fin varchar primary key,
nom_sit_fin varchar
)'''

createTsituacionR ='''CREATE TABLE situacionR(
sit_fin_r varchar primary key,
nom_sit_fin_r varchar
)'''

createTmencion ='''CREATE TABLE mencion(
cod_men varchar primary key,
nom_men varchar
)'''

createTfact_rendimiento ='''CREATE TABLE fact_rendimiento(
cod_rendimiento int primary key,
agno int,
cod_establecimiento int,
cod_curso int,
cod_alumno int,

asistencia int,

sit_fin varchar, --se puede traducir, situacion
sit_fin_r varchar, --se puede traducir, situacion
cod_men varchar, --se puede traducir, solo en 2019

cod_espe int,
cod_rama int,
cod_sec int,

prom_gral varchar,


foreign key (agno) references agno(agno),
foreign key (cod_establecimiento) references establecimiento(rbd),
foreign key (cod_curso) references curso(cod_curso),
foreign key (cod_alumno) references alumno(mrun),

foreign key (cod_espe) references especialidad(cod_espe),
foreign key (cod_rama) references rama(cod_rama),
foreign key (cod_sec) references sector(cod_sec),


foreign key (sit_fin) references situacion(sit_fin),
foreign key (sit_fin_r) references situacionR(sit_fin_r),
foreign key (cod_men) references mencion(cod_men)
)'''

