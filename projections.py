class Projection:

    GET_PROJECTION_BY_ID = '''
    SELECT id, projection_date, projection_time, projection_type
    FROM Projections
    WHERE movie_id=?
    ORDER BY projection_date '''

    GET_PROJECTION_ON_DATE = '''
    SELECT id, projection_time, projection_type
    FROM Projections
    WHERE movie_id=? and projection_date=?
    ORDER BY projection_date '''

    GET_PROJECTION_BY_P_ID = '''
    SELECT projection_date, projection_time, projection_type
    FROM Projections
    WHERE id=? '''

    @classmethod
    def get_projection_from_db(cls, conn, m_id):
        cursor = conn.cursor()
        # if 2 == len(filters):
        #     result = cursor.execute(cls.GET_PROJECTION_ON_DATE,
        #                             (filters[0], filters[1]))
        # elif 1 == len(filters):
        #
        cursor.execute(cls.GET_PROJECTION_BY_ID, (m_id, ))

        return cursor.fetchall()

    @classmethod
    def get_projection_by_id(cls, conn, p_id):
        cursor = conn.cursor()
        cursor.execute(cls.GET_PROJECTION_BY_P_ID, (p_id, ))

        return cursor.fetchall()[0]
