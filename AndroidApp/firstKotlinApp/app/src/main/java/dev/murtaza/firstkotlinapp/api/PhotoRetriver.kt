package dev.murtaza.firstkotlinapp.api

import dev.murtaza.firstkotlinapp.models.PhotoList
import retrofit2.Callback
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class PhotoRetriver {
    private val service: PhotoApi

    init {
        val retrofit = Retrofit.Builder().baseUrl("https://pixabay.com/api/")
            .addConverterFactory(GsonConverterFactory.create()).build()

        service = retrofit.create(PhotoApi::class.java)
    }

    fun getPhotos(callback: Callback<PhotoList>){
        val call = service.getPhoto()
        call.enqueue(callback)
    }
}