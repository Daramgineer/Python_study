import pickle
profile_file = open('profile.pickle', 'wb')
profile = {'이름':'A', '나이':30, '취미':['탁구', '당구']}
print(profile)
pickle.dump(profile, profile_file) #profile에 있는 정보를 profile_file에 저장
profile_file.close()

profile_file = open('profile.pickle', 'rb')
profile = pickle.load(profile_file) #profile_file에 있는 정보를 profile에 저장
print(profile)
profile_file.close()