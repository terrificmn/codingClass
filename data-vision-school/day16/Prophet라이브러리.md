# Prophet 라이브러리
- FACEBOOK에서 만든 Prophet 라이브러리 
- Seasonal time series data를 분석
- 딥러닝 라이브러리

- Seasonal time series data를 분석할 수 있는 딥러닝 라이브러리다. 
- 프로펫 공식 페이지 :  
 https://research.fb.com/prophet-forecasting-at-scale/
 https://facebook.github.io/prophet/docs/quick_start.html#python-api

## 설치
```
pip install fbprophet
또는 
conda install -c conda-forge fbprophet
```

## 불러오기
캐글의 Crimes in Chicago 의 데이터를 분석
파일은 
먼저 파일을 읽어오자
```py
df_CC_2008_to_2011 = pd.read_csv('Chicago_Crimes_2008_to_2011.csv', error_bad_lines=False, index_col=0)
```
`error_bad_lines` 파라미터를 False 해주면  
Error tokenizing data. C error 발생하는 것을 무시한다

`index_col=0` 이 args를 빼고 하면 불 필요하게 0번째 컬럼이 자동으로 생성되는데 이를 방지

## 데이터프레임 합치기
캐글에 보면 원래 csv파일은 4개로 되어 있다.  

판다스의 `concat()` 은 행(row) 수가 다르더라도 컬럼이 같다면  
위 아래로 합칠 수 있다. `axis=1`로 해서 옆으로 컬럼 옆으로 합칠 수 있음

```py
chicago_df =  pd.concat([chicago_df_1, chicago_df_2, chicago_df_3] )
```

불필요한 컬럼은 제거한다  
```py
chicago_df.drop( ['Case Number', 'Case Number', 'IUCR', ....생략], axis=1, inplace=True )
```
`inplace=True`는 메모리에 바로 반영되게 저장시킨다   
`axis=1` 은 컬럼으로 삭제  


## 날짜 형식 바꾸기
`판다스.to_datetime` 
```py
# 날짜형식 변환해서 다시 저장
chicago_df['Date'] = pd.to_datetime(chicago_df['Date'], format= '%m/%d/%Y %I:%M:%S %p')
```

'Date'컬럼을 인덱스로 지정. 여기서 인덱스는 row의 인덱스를 말한다  
`pd.DatetimeIndex( df['컬럼명'] )
```py
chicago_df.index = pd.DatetimeIndex(chicago_df['Date'])
```

## 비주얼 라이징
'Primary Type' 컬럼은 범죄의 유형인데 seaborn의 모듈을 이용  
```py
sns.countplot(data = chicago_df, y='Primary Type', order= chicago_df['Primary Type'].value_counts().index )
plt.show()

```
여기서 `order` 파라미터를 이용해서 정렬을 해줄 수 있는데 value_counts() 메소드로   
정렬이 된 데이터들의 인덱스를 넘겨준다    

응용 : `value_counts().head(10).index`  
위의 `order=` 파라미터에 위의 값을 넘겨주면 표시할 갯수도 지정할 수 있다  
즉 상위 10개만 보여줄 수 있음

## 리샘플링
`resample()` 메소드를 이용해서 몇개의 범죄의 데이터인지 확인
```py
year_df = chicago_df.resample('M').size()
```
위에서 넘겨준 'M' 값은 월을 의미

아래 표를 참고  

| Alias | Description |
| :--: | :-- |
| B | Business day |
| D | Calendar day |
| W | Weekly |
| M | Month end |
| Q | Quarter end |
| A | Year end |
| BA | Business year end |
| AS | Year start |
| H | Hourly frequency |
| T, min | Minutely frequency |
| S | Secondly frequency |
| L, ms | Millisecond frequency |
| U, us | Microsecond frequency |
| N, ns | Nanosecond frequency |

## 달별 주기 데이터프레임 만들기
위에서 설정했던 index 값을 리셋
```py
month_df = month_df.reset_index()
```

이제 컬럼 값이 온전하지 않을 수도 있는데 상관없다  
**Prophet** 라이브러리 규칙대로 컬럼명을 정해줘야 한다.  

시계열 예측이므로 날짜 컬럶은 *ds*  
예측하려는 수치는 *y* 로 바꿔준다

```py
# columns 속성을 이용
month_df.columns = ['ds', 'y']

# 또는 rename()메소드 이용, 이때는 딕셔너리 형태로 가공
chicago_prophet = month_df.rename(columns={'Date': 'ds', 0: 'y'})
```


## Prophet 예측
모듈 불러오기
```py
from fbprophet import Prophet
```

```py
# 객체 저장
m = Prophet()
# 위에서 만들어놓은 데이터프레임 학습
m.fit(chicago_prophet)

# freq='M' 으로 지정
future = m.make_future_dataframe(periods=36, freq='M')

forecast = m.predict(future)
```

이제 예측 결과를 볼 수 있음
```py
forecast
```
를 해보면 `yhat` 컬럼이 생겼는데 이는 예측한 데이터  
그외 trend, 	yhat_lower, 	yhat_upper, 	trend_lower, 	trend_upper 등의 컬럼이 생겼음

## 차트 크리기 
```py
예측한 데이터 
m.plot(forecast, xlabel='Monthly', ylabel='Crime rate')
```

트렌드와 yearly 로 데이터 차트 보기
```py
m.plot_components(forecast)
```




