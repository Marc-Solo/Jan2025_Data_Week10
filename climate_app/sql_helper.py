from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text

import pandas as pd

# Define the SQLHelper Class
# PURPOSE: Deal with all of the database logic

class SQLHelper():

    # Initialize PARAMETERS/VARIABLES

    #################################################
    # Database Setup
    #################################################
    def __init__(self):
        self.engine = create_engine("sqlite:///hawaii.sqlite")
        self.Station = self.createStation()
        self.Measurement = self.createMeasurement()

    # Used for ORM
    def createStation(self):
        # Reflect an existing database into a new model
        Base = automap_base()

        # reflect the tables
        Base.prepare(autoload_with=self.engine)

        # Save reference to the table
        Station = Base.classes.station
        return(Station)
    
    # Used for ORM
    def createMeasurement(self):
        # Reflect an existing database into a new model
        Base = automap_base()

        # reflect the tables
        Base.prepare(autoload_with=self.engine)

        # Save reference to the table
        Measurement = Base.classes.measurement
        return(Measurement)
    
    ##############################################################################################


    def queryPrecipitationORM(self):
        # Create our session (link) from Python to the DB
        session = Session(self.engine)

        # Query all precipitation
        rows = session.query(self.Measurement.id, self.Measurement.station,
                    self.Measurement.date, self.Measurement.prcp).filter(self.Measurement.date >= '2016-08-23').order_by(self.Measurement.date).all()

        # Create the dataframe
        df = pd.DataFrame(rows)

        # Close the Session
        session.close()
        return(df)

    # def queryPrecipitationSQL(self):
    #     # Create our session (link) from Python to the DB
    #     conn = self.engine.connect() # Raw SQL/Pandas

    #     # Define Query
    #     query = text("""SELECT
    #                     id,
    #                     station,
    #                     date,
    #                     prcp
    #                 FROM
    #                     measurement
    #                 WHERE
    #                     date >= '206-08-23'
    #                 ORDER BY
    #                     date;""")
    #     df = pd.read_sql(query, con=conn)

    #     # Close the connection
    #     conn.close()
    #     return(df)

    def queryStationsORM(self):
        # Create our session (link) from Python to the DB
        session = Session(self.engine)

        # Query all stations 
        rows = session.query(
            self.Station.station, self.Station.id, self.Station.name).order_by(self.Station.station).all()
        
        # Create the dataframe
        df = pd.DataFrame(rows)

        # Close the Session
        session.close()
        return(df)