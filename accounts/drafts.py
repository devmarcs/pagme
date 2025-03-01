# Aquivos do formulário de Secretaria do biddings
# def __init__(self, *args, **kwargs):
    #     self.mostrar_secretaria = kwargs.pop('mostrar_secretaria', False)
    #     super().__init__(*args, **kwargs)
    #     if not self.mostrar_secretaria:
    #         self.fields.pop('secretaria', None)

    #     if self.mostrar_secretaria:
    #         self.fields['secretaria'] = forms.ModelChoiceField(
    #             label="Secretaria",
    #             required=True,
    #             queryset=Secretaria.objects.all(),
    #             widget=forms.Select(
    #                 attrs={
    #                     "class": "form-control"
    #                 }
    #             )
    #         )
        # else:
        #     self.fields['secretaria'] = forms.ModelChoiceField(
        #         label="Secretaria",
        #         required=False,
        #         queryset=Secretaria.objects.all(),
        #         widget=forms.Select(
        #             attrs={
        #                 "class": "form-control"
        #             }
        #         )
        #     )

# Depois implementar o cadastro de usuário com e-mail, por agora não usar 
# Esse form é para atualizar o email do usuário
# class UpdateEmailForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['email']
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#         }


# View de cadastro de usuário
 # if User.objects.filter(email=email).exists():
            #     messages.error(request, "Email já cadastrado, use outro!")
            #     return render(request, "registration/cadastro.html", {"form": form})

# Depois implementar o menu do usuário, por agora apenas implementar o login e o cadastro
# class DetailMemberView(DetailView, PermissionRequiredMixin):
#     model = User
#     template_name = "usuario/detalhe_usuario.html"
#     context_object_name = "usuario"
#     permission_required = ["auth.view_user"]

#     def get_object(self):
#         # Exibe o usuário logado
#         return self.request.user

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['email_form'] = UpdateEmailForm(instance=self.request.user)
#         return context

#     def post(self, request, *args, **kwargs):
#         user = self.get_object()
#         # email_form = UpdateEmailForm(request.POST, instance=user)

#         if email_form.is_valid():
#             user = self.request.user
#             email_form.save()
#             messages.success(request, "Dados atualizados com sucesso!")
#             return redirect('usuarios:detail_member', user.pk)  # Redireciona após a atualização bem-sucedida

#         messages.error(request, "Dados inválidos, por favor verifique os dados!")
#         return self.render_to_response(self.get_context_data(email_form=email_form))

# View que lista os usuários logados
# Não serve para este projeto, até então
# class ListMemberView(ListView, PermissionRequiredMixin):
#     model = User
#     template_name = "usuario/list_usuarios.html"
#     context_object_name = "usuarios"
#     permission_required = ["auth.view_user"]