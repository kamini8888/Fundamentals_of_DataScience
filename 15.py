import pandas as pd
data={
    'post_likes' :[10, 15, 20, 12, 25, 20, 18, 30, 15, 10, 25],
    'customer_id': [1,2,3,4,5,6,7,8,9,10,11]
    }
df=pd.DataFrame(data)
print(df)
a=df['post_likes'].value_counts()
print("frequency distribution")
print(a)

OR

def calculate_likes_frequency(likes_list):
    likes_freq = {}
    for likes in likes_list:
        likes_freq[likes] = likes_freq.get(likes, 0) + 1
    return likes_freq

def display_likes_frequency_distribution(likes_freq):
    print("Likes\tFrequency")
    for likes, freq in likes_freq.items():
        print(f"{likes}\t{freq}")

if __name__ == "__main__":
    post_likes = [100, 150, 200, 120, 250, 200, 180, 300, 150, 100, 250]
    likes_frequency = calculate_likes_frequency(post_likes)
    display_likes_frequency_distribution(likes_frequency)
