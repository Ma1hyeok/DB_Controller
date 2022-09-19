from db_manager import EngineFactory
from environs import Environ
from db_manager import SessionMaker
from sqlalchemy.ext.declarative import declarative_base

import pandas as pd


engine = EngineFactory.create_engine_DATA_by('data_mig', echo=True)
Base = declarative_base(engine)


class V3GameCode(Base):
    __tablename__ = 'oper_games'
    __table_args__ = {"autoload": True, 'extend_existing': True}


if __name__ == '__main__':
    engine = EngineFactory.create_engine_DATA_by(Environ.DATA_DB_NAME, echo= True)
    
    sql = f"""
    select id
    ,b4_code as 'game_id'
    , (case 
        when lang_subtitle is not null  then '1' 
        when lang_subtitle is null then '0' 
        end) as 'language_sub'
    , (case
        when lang_full_audio is not null  then '1' 
        when lang_full_audio is null then '0' 
        end) as 'language_audio'

        from
            (
            select g.id
            , b4_code
            , origin_id
            , sg.name_en
            , CAST( lang_full_audio AS CHAR (10000) CHARACTER SET UTF8) AS lang_full_audio
            , CAST( lang_subtitle AS CHAR (10000) CHARACTER SET UTF8) AS lang_subtitle

            from (select *
                    from hangar.b4_integrate_games
                    where source = 'steam') as i
                    inner join steam.steam_games_en as sg on i.source_id = sg.id
                    inner join data_mig.std_games_origin as sgo on sgo.origin_id = i.game_id
                    inner join data_mig.oper_games as g on g.game_id = sgo.b4_code)z
        
            where 
                    lang_full_audio like '%%korean%%'
            or 
                    lang_subtitle like '%%korean%%'

            group by 1
    """
    
    df = pd.read_sql(sql,engine)
    #df = df.set_index('b4_code',drop = True, append = False,verify_integrity=False)
    
    print(df)
    
    #engine.close()
        
    def row_run():
        buf = []
        with SessionMaker(engine) as session:
            game = session.query(V3GameCode)
            #df = pd.read_sql(game.statement, game.session.bind)
            for row in df.to_dict('records'):
                data = {"id": row['id'], "language_audio": 1, "language_sub":1}
                buf.append(data)
            a= session.bulk_update_mappings(V3GameCode, buf)
            print(data)
            #session.flush()
            session.commit()
            return df
        


    print(row_run())