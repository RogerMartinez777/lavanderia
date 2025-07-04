USE [LavanderiaBeatriz]
GO
/****** Object:  Table [dbo].[Acolchados]    Script Date: 30/06/2025 18:28:07 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Acolchados](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[descripcion] [varchar](50) NOT NULL,
	[id_precio] [int] NOT NULL,
	[id_tamanio] [int] NOT NULL,
 CONSTRAINT [PK_Acolchados] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Clientes]    Script Date: 30/06/2025 18:28:07 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Clientes](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[nombre] [varchar](50) NOT NULL,
	[apellido] [varchar](50) NULL,
	[telefono] [varchar](50) NULL,
	[mail] [varchar](50) NULL,
 CONSTRAINT [PK_Clientes] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Detalles_Lavado]    Script Date: 30/06/2025 18:28:07 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Detalles_Lavado](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[nro_lavado] [int] NOT NULL,
	[cantidad] [int] NOT NULL,
	[id_acolchado] [int] NOT NULL,
 CONSTRAINT [PK_Detalles_Lavado] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Encargados_Recep]    Script Date: 30/06/2025 18:28:07 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Encargados_Recep](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[nombre] [varchar](50) NOT NULL,
	[apellido] [varchar](50) NOT NULL,
	[alias] [varchar](50) NULL,
	[fecha_nacimiento] [date] NULL,
	[estado] [bit] NOT NULL,
	[id_Puesto] [int] NOT NULL,
 CONSTRAINT [PK_Encargados_Recep] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Estados_Lavado]    Script Date: 30/06/2025 18:28:07 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Estados_Lavado](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[descripcion] [varchar](50) NOT NULL,
 CONSTRAINT [PK_Estados_Lavado] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Lavados]    Script Date: 30/06/2025 18:28:07 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Lavados](
	[nro_lavado] [int] IDENTITY(1,1) NOT NULL,
	[fecha] [date] NOT NULL,
	[total] [decimal](10, 2) NOT NULL,
	[estado] [int] NOT NULL,
	[id_encargado_recep] [int] NOT NULL,
	[id_cliente] [int] NOT NULL,
	[id_tipo_cobro] [int] NOT NULL,
	[id_estado] [int] NOT NULL,
 CONSTRAINT [PK_Lavados] PRIMARY KEY CLUSTERED 
(
	[nro_lavado] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Precios]    Script Date: 30/06/2025 18:28:07 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Precios](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[precio] [decimal](18, 0) NOT NULL,
 CONSTRAINT [PK_Precios] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Tamanios]    Script Date: 30/06/2025 18:28:07 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Tamanios](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[descripcion] [varchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Tipos_Cobro]    Script Date: 30/06/2025 18:28:07 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Tipos_Cobro](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[descripcion] [varchar](50) NOT NULL,
 CONSTRAINT [PK_Tipos_Pago] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Tipos_Puesto]    Script Date: 30/06/2025 18:28:07 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Tipos_Puesto](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[descripcion] [varchar](50) NOT NULL,
 CONSTRAINT [PK_Tipos_Puesto] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[usuarios]    Script Date: 30/06/2025 18:28:07 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[usuarios](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[username] [varchar](50) NOT NULL,
	[password] [varchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[Clientes] ON 

INSERT [dbo].[Clientes] ([id], [nombre], [apellido], [telefono], [mail]) VALUES (1, N'Viejo', N'Pupero', N'3515469874', N'viejopupero@yahoo.com.ar')
INSERT [dbo].[Clientes] ([id], [nombre], [apellido], [telefono], [mail]) VALUES (2, N'Roger', N'Martinez', N'3512539777', N'rogermartinez1357@gmail.com')
INSERT [dbo].[Clientes] ([id], [nombre], [apellido], [telefono], [mail]) VALUES (4, N'Yuliana', N'Selever', N'3513369333', N'yulianaselever@gmail.com')
INSERT [dbo].[Clientes] ([id], [nombre], [apellido], [telefono], [mail]) VALUES (5, N'Nicolas', N'Martinez', N'3512984512', N'nicofedericom@gmail.com')
INSERT [dbo].[Clientes] ([id], [nombre], [apellido], [telefono], [mail]) VALUES (6, N'Paloma', N'Selever', N'3516983214', N'pobremiaumiau@yahoo.com.ar')
INSERT [dbo].[Clientes] ([id], [nombre], [apellido], [telefono], [mail]) VALUES (7, N'Noelia', N'Selever', N'3516987111', N'noeselever@yahoo.com.ar')
INSERT [dbo].[Clientes] ([id], [nombre], [apellido], [telefono], [mail]) VALUES (8, N'Matias', N'Quercia', N'01187966545', N'matiasquercia@outlook.com.ar')
SET IDENTITY_INSERT [dbo].[Clientes] OFF
GO
SET IDENTITY_INSERT [dbo].[Encargados_Recep] ON 

INSERT [dbo].[Encargados_Recep] ([id], [nombre], [apellido], [alias], [fecha_nacimiento], [estado], [id_Puesto]) VALUES (1, N'Beatriz', N'Selever', N'Magre', CAST(N'1960-05-02' AS Date), 1, 1)
INSERT [dbo].[Encargados_Recep] ([id], [nombre], [apellido], [alias], [fecha_nacimiento], [estado], [id_Puesto]) VALUES (2, N'Yuliana', N'Martinez', N'Yuli', CAST(N'1988-10-17' AS Date), 1, 2)
INSERT [dbo].[Encargados_Recep] ([id], [nombre], [apellido], [alias], [fecha_nacimiento], [estado], [id_Puesto]) VALUES (3, N'Nicolas', N'Martinez', N'Nico', CAST(N'2000-01-12' AS Date), 1, 3)
INSERT [dbo].[Encargados_Recep] ([id], [nombre], [apellido], [alias], [fecha_nacimiento], [estado], [id_Puesto]) VALUES (4, N'Paloma', N'Selever', N'MiauMiauMiau', NULL, 1, 2)
INSERT [dbo].[Encargados_Recep] ([id], [nombre], [apellido], [alias], [fecha_nacimiento], [estado], [id_Puesto]) VALUES (5, N'Noelia', N'Martinez', NULL, NULL, 0, 3)
SET IDENTITY_INSERT [dbo].[Encargados_Recep] OFF
GO
SET IDENTITY_INSERT [dbo].[Precios] ON 

INSERT [dbo].[Precios] ([id], [precio]) VALUES (1, CAST(10000 AS Decimal(18, 0)))
INSERT [dbo].[Precios] ([id], [precio]) VALUES (2, CAST(12000 AS Decimal(18, 0)))
INSERT [dbo].[Precios] ([id], [precio]) VALUES (3, CAST(16000 AS Decimal(18, 0)))
SET IDENTITY_INSERT [dbo].[Precios] OFF
GO
SET IDENTITY_INSERT [dbo].[Tamanios] ON 

INSERT [dbo].[Tamanios] ([id], [descripcion]) VALUES (1, N'1 Plaza')
INSERT [dbo].[Tamanios] ([id], [descripcion]) VALUES (2, N'2 Plazas')
INSERT [dbo].[Tamanios] ([id], [descripcion]) VALUES (3, N'2,5 Plazas ')
INSERT [dbo].[Tamanios] ([id], [descripcion]) VALUES (4, N'Otros')
SET IDENTITY_INSERT [dbo].[Tamanios] OFF
GO
SET IDENTITY_INSERT [dbo].[Tipos_Cobro] ON 

INSERT [dbo].[Tipos_Cobro] ([id], [descripcion]) VALUES (1, N'Efectivo')
INSERT [dbo].[Tipos_Cobro] ([id], [descripcion]) VALUES (2, N'Transferencia')
SET IDENTITY_INSERT [dbo].[Tipos_Cobro] OFF
GO
SET IDENTITY_INSERT [dbo].[Tipos_Puesto] ON 

INSERT [dbo].[Tipos_Puesto] ([id], [descripcion]) VALUES (1, N'Gerente')
INSERT [dbo].[Tipos_Puesto] ([id], [descripcion]) VALUES (2, N'Supervisor')
INSERT [dbo].[Tipos_Puesto] ([id], [descripcion]) VALUES (3, N'Operario')
SET IDENTITY_INSERT [dbo].[Tipos_Puesto] OFF
GO
SET IDENTITY_INSERT [dbo].[usuarios] ON 

INSERT [dbo].[usuarios] ([id], [username], [password]) VALUES (1, N'roger', N'369')
SET IDENTITY_INSERT [dbo].[usuarios] OFF
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ__usuarios__F3DBC572FA50229F]    Script Date: 30/06/2025 18:28:07 ******/
ALTER TABLE [dbo].[usuarios] ADD UNIQUE NONCLUSTERED 
(
	[username] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Encargados_Recep] ADD  CONSTRAINT [DF__Encargado__estad__32AB8735]  DEFAULT ((1)) FOR [estado]
GO
ALTER TABLE [dbo].[Acolchados]  WITH CHECK ADD  CONSTRAINT [FK_Acolchados_Tamanio] FOREIGN KEY([id_tamanio])
REFERENCES [dbo].[Tamanios] ([id])
GO
ALTER TABLE [dbo].[Acolchados] CHECK CONSTRAINT [FK_Acolchados_Tamanio]
GO
ALTER TABLE [dbo].[Detalles_Lavado]  WITH CHECK ADD  CONSTRAINT [FK_Detalles_Lavado_Acolchados] FOREIGN KEY([id_acolchado])
REFERENCES [dbo].[Acolchados] ([id])
GO
ALTER TABLE [dbo].[Detalles_Lavado] CHECK CONSTRAINT [FK_Detalles_Lavado_Acolchados]
GO
ALTER TABLE [dbo].[Detalles_Lavado]  WITH CHECK ADD  CONSTRAINT [FK_Detalles_Lavado_Lavado] FOREIGN KEY([nro_lavado])
REFERENCES [dbo].[Lavados] ([nro_lavado])
GO
ALTER TABLE [dbo].[Detalles_Lavado] CHECK CONSTRAINT [FK_Detalles_Lavado_Lavado]
GO
ALTER TABLE [dbo].[Encargados_Recep]  WITH CHECK ADD  CONSTRAINT [FK_Encargados_Recep_Tipos_Puesto] FOREIGN KEY([id_Puesto])
REFERENCES [dbo].[Tipos_Puesto] ([id])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[Encargados_Recep] CHECK CONSTRAINT [FK_Encargados_Recep_Tipos_Puesto]
GO
ALTER TABLE [dbo].[Lavados]  WITH CHECK ADD  CONSTRAINT [FK_Lavados_Clientes] FOREIGN KEY([id_cliente])
REFERENCES [dbo].[Clientes] ([id])
GO
ALTER TABLE [dbo].[Lavados] CHECK CONSTRAINT [FK_Lavados_Clientes]
GO
ALTER TABLE [dbo].[Lavados]  WITH CHECK ADD  CONSTRAINT [FK_Lavados_Encargados_Recep] FOREIGN KEY([id_encargado_recep])
REFERENCES [dbo].[Encargados_Recep] ([id])
GO
ALTER TABLE [dbo].[Lavados] CHECK CONSTRAINT [FK_Lavados_Encargados_Recep]
GO
ALTER TABLE [dbo].[Lavados]  WITH CHECK ADD  CONSTRAINT [FK_Lavados_Estados_Lavado] FOREIGN KEY([id_estado])
REFERENCES [dbo].[Estados_Lavado] ([id])
GO
ALTER TABLE [dbo].[Lavados] CHECK CONSTRAINT [FK_Lavados_Estados_Lavado]
GO
ALTER TABLE [dbo].[Lavados]  WITH CHECK ADD  CONSTRAINT [FK_Lavados_Tipos_Cobro] FOREIGN KEY([id_tipo_cobro])
REFERENCES [dbo].[Tipos_Cobro] ([id])
GO
ALTER TABLE [dbo].[Lavados] CHECK CONSTRAINT [FK_Lavados_Tipos_Cobro]
GO
