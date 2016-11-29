from pandas import Series, DataFrame

kakao2 = Series([92600, 92400, 92100, 94300, 92300], index=['2016-02-19',
                                                            '2016-02-18',
                                                            '2016-02-17',
                                                            '2016-02-16',
                                                            '2016-02-15'])
#print(kakao2)

#print(kakao2['2016-02-19'])
#print(kakao2['2016-02-18'])

for date in kakao2.index:
    print(date)

for ending_price in kakao2.values:
    print(ending_price)