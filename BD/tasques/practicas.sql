select etapes.numero, ciclistes.equip from etapes, ciclistes where etapes.ciclista = ciclistes.dorsal


select etapes.numero, equips.director from etapes, ciclistes, equips where etapes.ciclista = ciclistes.dorsal and ciclistes.equip = equips.nom;

sub_8) Mostra la informació dels ciclistes d’edat màxima de cada equip.

select ciclistes.nom, equip.nom from ciclistes, equip where max(edad) in (select ciclistes.edad from ciclistes);