from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 建立与MySQL的连接
host = "127.0.0.1"
db_name = "flask_jobs"
db_username = "root"
db_password = "root"
engine = create_engine(f'mysql+pymysql://{db_username}:{db_password}@{host}/{db_name}?charset=utf8',
                       echo=False,  # echo 设为 true 会打印出实际执行的 sql，调试的时候更方便
                       future=True,  # 使用 2.0API，向后兼容
                       pool_size=5,  # 连接池的大小默认为 5 个，设置为 0 时表示连接无限制
                       pool_recycle=3600,  # 多久之后对线程池中的线程进行一次连接的回收（重置）
                       pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
                       pool_pre_ping=True  # 悲观方式， 每次执行sql钱会检查连接,解决数据库异常回复后连接依然没有恢复问题
                       )
Base = declarative_base()


class Jobs(Base):
    __tablename__ = 'jobs'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = Column(Integer, primary_key=True)
    jobName = Column(String(500), nullable=False)
    highMonthPay = Column(String(500), nullable=False)
    updateDate = Column(String(500), nullable=False)
    lowMonthPay = Column(String(500), nullable=False)
    headCount = Column(String(500), nullable=False)
    publishDate = Column(String(500), nullable=False)
    degreeName = Column(String(500), nullable=False)
    recName = Column(String(500), nullable=False)
    recLogo = Column(String(500), nullable=False)
    areaCodeName = Column(String(500), nullable=False)
    recScale = Column(String(500), nullable=False)
    recTags = Column(String(500), nullable=False)
    major = Column(String(500), nullable=False)
    recProperty = Column(String(500), nullable=False)


db_session = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True, expire_on_commit=False)()
#Base.metadata.drop_all(engine)
#Base.metadata.create_all(engine)
db_session.commit()
db_session.close()
