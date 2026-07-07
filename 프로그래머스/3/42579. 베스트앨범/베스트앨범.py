def solution(genres, plays):
    answer = []
    genre_total = {}
    genre_song = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        genre_total[genre] = genre_total.get(genre, 0) + play
        
        if genre not in genre_song:
            genre_song[genre] = []
        genre_song[genre].append((play, i))
        
    sorted_genres = sorted(genre_total.items(), key=lambda x: x[1], reverse=True)
    
    for genre, _ in sorted_genres:
        songs = sorted(genre_song[genre], key=lambda x: (-x[0], x[1]))
        
        for play, idx in songs[:2]:
            answer.append(idx)
            
    return answer